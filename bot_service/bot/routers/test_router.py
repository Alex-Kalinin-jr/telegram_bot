import logging
import os

from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import FSInputFile
from aiogram.exceptions import TelegramBadRequest
from aiogram import flags

from middlewares.logging_middleware import handle_outer_middleware, logging_middleware
from keyboards.keyboards import get_keyboard, get_positions_kb
from data.button_name import kb_main_menu
from utils.utils import get_language
from database.db import BotDB
from services.db import Interactor


logger = logging.getLogger(__name__)
router = Router()
router.message.outer_middleware(handle_outer_middleware)
router.callback_query.outer_middleware(handle_outer_middleware)
router.message.middleware(logging_middleware)
router.callback_query.middleware(logging_middleware)

names = get_language()

main_menu_markup = get_keyboard(kb_main_menu)
only_back_menu_markup = get_keyboard(["back"])

#this should be refactored. 
# When new position is added - reply markup should be rebuilded. but at working time it should be static
price_menu_markup = 2
categories_menu_markup = 1
#******

class FsmFillForm(StatesGroup):
    category = State()
    nomenclature = State()
    contacts = State()
    category_info = State()
    position_info = State()


@flags.chat_action
async def command_start_replace(message: Message, state: FSMContext):
    try:
        await state.clear()
        await message.edit_text(f'Hi {message.from_user.full_name}!', reply_markup=main_menu_markup)

    except TelegramBadRequest as e:
        logger.error(f"command_start_replace - error was detected: {e}")


@router.message(CommandStart(),)
async def command_start(message: Message, state: FSMContext):
    try:
        await state.clear()
        await message.answer(f'Hi {message.from_user.full_name}!', reply_markup=main_menu_markup)
        return True
    except TelegramBadRequest as e:
        logger.error(f"command_start_replace - error was detected: {e}")


@router.callback_query(F.data == "back",)
async def answer_price(call: CallbackQuery, state: FSMContext, db_service: Interactor,):
    state_str = await state.get_state()
    
    try:
        if state_str in [FsmFillForm.category, FsmFillForm.contacts]:
            await state.clear()
            await command_start_replace(call.message, state)
        elif state_str in [FsmFillForm.category_info, FsmFillForm.nomenclature]:
            print("\n\ni was here")
            await state.set_state(FsmFillForm.category)
            await answer_categories(call, db_service, state)
            print("\n\ni was here")
        elif state_str in [FsmFillForm.position_info]:
            await state.set_state(FsmFillForm.nomenclature)
            await answer_nomenclature(call, db_service, state)
    except TelegramBadRequest as e:
        logger.error(f"command_start_replace - error was detected: {e}")
        
        
@router.callback_query(F.data == "contacts", StateFilter(default_state),)
async def answer_contacts(call: CallbackQuery, state: FSMContext):
    try:
        await state.set_state(FsmFillForm.contacts)
        await call.message.edit_text(names['contacts'], reply_markup=only_back_menu_markup)
    except TelegramBadRequest as e:
        logger.error(f"command_start_replace - error was detected: {e}")


@router.callback_query(F.data == "price_list", StateFilter(default_state),)
async def answer_categories(call: CallbackQuery, db_service: Interactor, state: FSMContext):
    try:
        response = db_service.get_categories()
        data_dict: dict = {i["name"]: i["name"] for i in response}
        await call.message.edit_text(names['categories'], reply_markup=get_positions_kb(data_dict))
        await state.set_state(FsmFillForm.category)
    except TelegramBadRequest as e:
        logger.error(f"command_start_replace - error was detected: {e}")


# see Models.py of db_service
@router.callback_query(StateFilter(FsmFillForm.nomenclature),)
async def get_position_info(call: CallbackQuery, db_service: Interactor, bot: Bot):
    try:
        data_description = db_service.get_position_by_its_name(call.data) #this
        data = db_service.get_position_photos(call.data) #this
        category = db_service.get_category_by_id(data_description["category_id"]) #this
        path = os.getcwd()
        for i in data:
            file_path = os.path.join(path, "bot/images", i["img"])
            photo = FSInputFile(file_path, filename="image")
            if photo:
                await call.message.answer_photo(photo)

        keyboard = call.message.reply_markup

        await call.message.answer(data_description["description"], reply_markup=keyboard)
        await bot.delete_message(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )

    except Exception as e:
        logger.error(f"get_position_info - error was detected: {e}")
        

@router.callback_query(F.data != "back", StateFilter(FsmFillForm.category),)
async def answer_nomenclature(call: CallbackQuery, db_instance: BotDB, state: FSMContext, db_service: Interactor):
    data = db_service.get_description_by_category(call.data)
    nomenclature_data = db_service.get_data_by_category(data["name"])
    nomenclature_data_dict: dict = {i["position"]: i["position"] for i in nomenclature_data}
    try:
        await call.message.edit_text(data["description"], reply_markup=get_positions_kb(nomenclature_data_dict))
        await state.set_state(FsmFillForm.nomenclature)
    except TelegramBadRequest as e:
        logger.error(f"command_start_replace - error was detected: {e}")


# @router.callback_query()
# async def answer_default(call: CallbackQuery):
#     print(call.model_dump_json(indent=4, exclude_none=True))


# @router.message()
# async def answer_default(message: Message):
#     await message.answer(f"Hi {message.from_user.id}!")