import logging

from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup


from keyboards.keyboards import get_price_list_kb, get_keyboard
from data.button_name import kb_main_menu
from utils.utils import get_language
from database.db import BotDB

logger = logging.getLogger(__name__)
router = Router()
names = get_language()

class FsmFillForm(StatesGroup):
    category = State()
    nomenclature = State()
    certain_position = State()


@router.message(CommandStart(), StateFilter(default_state))
async def command_start(message: Message):
    await message.answer(f'Hi {message.from_user.full_name}!', reply_markup=get_keyboard(kb_main_menu))
    
    
@router.callback_query(F.data == "contacts", StateFilter(default_state))
async def answer_contacts(call: CallbackQuery):
    await call.message.edit_text(names['contacts'], reply_markup=get_keyboard(["back"]))
    

@router.callback_query(F.data == "price_list", StateFilter(default_state))
async def answer_categories(call: CallbackQuery, db_instance: BotDB, state: FSMContext):
    data_dict: dict = {i[0]: i[0] for i in db_instance.get_categories()}
    await call.message.edit_text(names['categories'], reply_markup=get_price_list_kb(data_dict))
    await state.set_state(FsmFillForm.category)
    

@router.callback_query(F.data != "back", StateFilter(FsmFillForm.category))
async def answer_nomenclature(call: CallbackQuery, db_instance: BotDB, state: FSMContext):
    logger.debug(f"function call is in ANSWER_NOMENCLATURE")
    data = db_instance.get_data_by_category(call.data)
    data_dict: dict = {i[2]: i[0] for i in data}
    await call.message.edit_text(names['price_list'], reply_markup=get_price_list_kb(data_dict))
    await state.set_state(FsmFillForm.nomenclature)
    

# @router.callback_query(StateFilter(FsmFillForm.certain_position))
#     async def answer_certain_position(call: CallbackQuery, state: FSMContext):
        

   
@router.callback_query(F.data == "back", ~StateFilter(default_state))
async def answer_price(call: CallbackQuery, db_instance: BotDB, state: FSMContext):
    state_str = await state.get_state()
    
    if state_str == FsmFillForm.category:
        await state.clear()
        await call.message.edit_text(names['main_menu'], reply_markup=get_keyboard(kb_main_menu))
    elif state_str == FsmFillForm.nomenclature:
        await state.set_state(FsmFillForm.category)
        categories_dict: dict = {i[0]: i[0] for i in db_instance.get_categories()}
        await call.message.edit_text(names['categories'], reply_markup=get_price_list_kb(categories_dict))
        
    
    
@router.callback_query(F.data == "main_menu")
async def answer_main_menu(call: CallbackQuery):
    await call.message.edit_text(names['main_menu'], reply_markup=get_keyboard(kb_main_menu))