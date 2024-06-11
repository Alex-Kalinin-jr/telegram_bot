import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from middlewares.admin_middleware import AdmMiddleware
from keyboards.keyboards import get_keyboard
from data.button_name import kb_admin_main_menu

logger = logging.getLogger(__name__)
r_admin = Router()
r_admin.message.outer_middleware(AdmMiddleware())
r_admin.callback_query.outer_middleware(AdmMiddleware())

class FsmAdmin(StatesGroup):
    admin_mode = State()


@r_admin.message(Command(commands=['admin']))
async def command_admin(message: Message, state: FSMContext):
    state.set_state(FsmAdmin.admin_mode)
    await message.answer('Admin panel', reply_markup=get_keyboard(kb_admin_main_menu))

@r_admin.callback_query(F.data == 'back', StateFilter(FsmAdmin.admin_mode))
async def answer_back(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await command_admin(call.message, state)
    await call.message.edit_text('Admin panel', reply_markup=get_keyboard(kb_admin_main_menu))

@r_admin.callback_query(F.data == 'add_position', StateFilter(FsmAdmin.admin_mode))
async def answer_add_position(call: CallbackQuery, state: FSMContext):
    await call.message.answer("this is the mock for the add position")

# block user
# unblock user
# add user as admin
# delete user from admins list
# delete position
# delete category
# add new category
# add new position