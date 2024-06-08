from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from keyboards.keyboards import get_price_list_kb, get_keyboard
from data.button_name import kb_main_menu
from utils.utils import get_language

router = Router()

names = get_language()

@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(f'Hi {message.from_user.full_name}!', reply_markup=get_keyboard(kb_main_menu))
    
    
@router.callback_query(F.data == "contacts")
async def answer_contacts(call: CallbackQuery):
    await call.message.edit_text(names['contacts'], reply_markup=get_keyboard(["back"]))
    
    
@router.callback_query(F.data == "price_list")
async def answer_price(call: CallbackQuery):
    await call.message.edit_text(names['price_list'], reply_markup=get_price_list_kb({}))
    
    
@router.callback_query(F.data == "back")
async def answer_price(call: CallbackQuery):
    await call.message.edit_text(names['back'], reply_markup=get_keyboard(kb_main_menu))
    
    
@router.callback_query(F.data == "main_menu")
async def answer_main_menu(call: CallbackQuery):
    await call.message.edit_text(names['main_menu'], reply_markup=get_keyboard(kb_main_menu))