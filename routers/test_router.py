import logging
import requests
import json
import os

from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import FSInputFile

from keyboards.keyboards import get_price_list_kb, get_keyboard
from data.button_name import kb_main_menu
from utils.utils import get_language
from database.db import BotDB
from keyboards.keyboards import MyCallbackFactory
from config import BOT_TOKEN

logger = logging.getLogger(__name__)
router = Router()
names = get_language()

class FsmFillForm(StatesGroup):
    category = State()
    nomenclature = State()
    certain_position = State()
    contacts = State()
    category_info = State()
    position_info = State()


async def command_start_replace(message: Message):
    await message.edit_text(f'Hi {message.from_user.full_name}!', reply_markup=get_keyboard(kb_main_menu))


@router.message(CommandStart(), StateFilter(default_state))
async def command_start(message: Message):
    await message.answer(f'Hi {message.from_user.full_name}!', reply_markup=get_keyboard(kb_main_menu))
    
    
@router.callback_query(F.data == "back")
async def answer_price(call: CallbackQuery, db_instance: BotDB, state: FSMContext):
    state_str = await state.get_state()
    
    if state_str in [FsmFillForm.category, FsmFillForm.contacts]:
        await state.clear()
        await command_start_replace(call.message)
    elif state_str in [FsmFillForm.nomenclature, FsmFillForm.category_info]:
        await state.set_state(FsmFillForm.category)
        await answer_categories(call, db_instance, state)
    elif state_str in [FsmFillForm.position_info]:
        await state.set_state(FsmFillForm.nomenclature)
        await answer_nomenclature(call, db_instance, state)
        
        
@router.callback_query(F.data == "contacts", StateFilter(default_state))
async def answer_contacts(call: CallbackQuery, state: FSMContext):
    await state.set_state(FsmFillForm.contacts)
    await call.message.edit_text(names['contacts'], reply_markup=get_keyboard(["back"]))
    

@router.callback_query(F.data == "price_list", StateFilter(default_state))
async def answer_categories(call: CallbackQuery, db_instance: BotDB, state: FSMContext):
    data_dict: dict = {i[0]: i[0] for i in db_instance.get_categories()}
    await call.message.edit_text(names['categories'], reply_markup=get_price_list_kb(data_dict))
    await state.set_state(FsmFillForm.category)
    

@router.callback_query(MyCallbackFactory.filter(F.action == "get_info"), StateFilter(FsmFillForm.category))
async def get_category_info(call: CallbackQuery, db_instance: BotDB, state: FSMContext, callback_data: MyCallbackFactory):
    await state.set_state(FsmFillForm.category_info)
    data = db_instance.get_description_by_category(callback_data.item_id)
    await call.message.edit_text(data[0], reply_markup=get_keyboard(["back"]))
    

@router.callback_query(MyCallbackFactory.filter(F.action == "get_info"), StateFilter(FsmFillForm.nomenclature))
async def get_position_info(call: CallbackQuery, db_instance: BotDB, state: FSMContext, callback_data: MyCallbackFactory):
    await state.set_state(FsmFillForm.position_info)
    data = db_instance.get_description_by_position(callback_data.item_id)
    await call.message.edit_text(data[0], reply_markup=get_keyboard(["back"]))


@router.callback_query(F.data != "back", StateFilter(FsmFillForm.category))
async def answer_nomenclature(call: CallbackQuery, db_instance: BotDB, state: FSMContext):
    data_dict: dict = {i[2]: i[0] for i in db_instance.get_data_by_category(call.data)}
    await call.message.edit_text(names['price_list'], reply_markup=get_price_list_kb(data_dict))
    await state.set_state(FsmFillForm.nomenclature)
        
     
@router.callback_query(F.data == "main_menu")
async def answer_main_menu(call: CallbackQuery):
    await call.message.edit_text(names['main_menu'], reply_markup=get_keyboard(kb_main_menu))
    

@router.callback_query(StateFilter(FsmFillForm.nomenclature))
async def answer_position(call: CallbackQuery, db_instance: BotDB, state: FSMContext):
    data = db_instance.get_position_photos(call.data)
    path = os.getcwd()
    for i in data:
        file_path = os.path.join(path, "images", i[1])
        photo = FSInputFile(file_path, filename="image")
        await call.message.answer_photo(photo)
    
@router.callback_query()
async def answer_default(call: CallbackQuery):
    print(call.model_dump_json(indent=4, exclude_none=True))