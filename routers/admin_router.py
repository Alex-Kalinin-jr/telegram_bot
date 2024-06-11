import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from middlewares.admin_middleware import AdmMiddleware
from keyboards.keyboards import get_keyboard
from data.button_name import kb_admin_main_menu
from utils.utils import get_admin_messages
from data.button_name import dict_messages
from database.db import BotDB

MESSAGES = get_admin_messages()

logger = logging.getLogger(__name__)
r_admin = Router()
r_admin.message.outer_middleware(AdmMiddleware())
r_admin.callback_query.outer_middleware(AdmMiddleware())

only_back_menu_markup=get_keyboard(["back"])

class FsmAdmin(StatesGroup):
    admin_mode_start = State()
    add_category = State()


@r_admin.message(Command(commands=['admin']))
async def command_admin(message: Message, state: FSMContext):
    state.set_state(FsmAdmin.admin_mode_start)
    await message.answer('Admin panel', reply_markup=get_keyboard(kb_admin_main_menu))


@r_admin.callback_query(F.data == 'back', StateFilter(FsmAdmin.add_category))
async def answer_back(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await command_admin(call.message, state)
    await call.message.edit_text('Admin panel', reply_markup=get_keyboard(kb_admin_main_menu))


@r_admin.callback_query(F.data == "add_category", StateFilter(FsmAdmin.admin_mode_start))
async def add_new_category(call: CallbackQuery, state: FSMContext):
    await state.set_state(FsmAdmin.add_category)
    await call.message.edit_text(MESSAGES["add_category_1"], reply_markup=only_back_menu_markup)


@r_admin.callback_query(StateFilter(FsmAdmin.add_category))
async def check_and_write_category(call: CallbackQuery, db_instance: BotDB):
    categories = await db_instance.get_categories()
    if call.message.text in categories:
        await call.message.edit_text(MESSAGES['add_category_already_exist'], reply_markup=only_back_menu_markup)
    else:
        await call.message.edit_text(text="mock", reply_markup=only_back_menu_markup)


@r_admin.callback_query()
async def debug_function(call: CallbackQuery):
    print(call.model_dump_json(indent=4), exclude_none=True)

#IN FUTURE
# block user
# unblock user
# add user as admin
# delete user from admins list

#NOW
# delete position
# delete category
# add new category
# add new position