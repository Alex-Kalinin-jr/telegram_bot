import logging

from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from middlewares.admin_middleware import AdmMiddleware
from keyboards.keyboards import get_keyboard
from data.button_name import kb_admin_main_menu
from utils.utils import get_admin_messages
from database.db import BotDB
from middlewares.logging_middleware import handle_outer_middleware, logging_middleware


logger = logging.getLogger(__name__)

MESSAGES = get_admin_messages()

r_admin = Router()
r_admin.message.outer_middleware(handle_outer_middleware)
r_admin.callback_query.outer_middleware(handle_outer_middleware)
r_admin.message.middleware(logging_middleware)
r_admin.callback_query.middleware(logging_middleware)

only_back_menu_markup=get_keyboard(["back"])
admin_menu_keyboard=get_keyboard(kb_admin_main_menu)

class FsmAdmin(StatesGroup):
    add_category = State()


@r_admin.message(Command(commands=['admin']),)
async def command_admin(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Admin panel', reply_markup=admin_menu_keyboard)


async def answer_command_admin(message: Message, state: FSMContext):
    await state.clear()
    await message.edit_text('Admin panel', reply_markup=admin_menu_keyboard)


@r_admin.callback_query(F.data=='back', StateFilter(FsmAdmin.add_category),)
async def answer_back(call: CallbackQuery, state: FSMContext, bot: Bot):
    await answer_command_admin(call.message, state)


@r_admin.callback_query(F.data=="add_category",)
async def add_new_category(call: CallbackQuery, state: FSMContext):
    await state.set_state(FsmAdmin.add_category)
    await call.message.edit_text(MESSAGES["add_category_1"], reply_markup=only_back_menu_markup)



#here to be continued
#here to be continued
#here to be continued
#here to be continued
#here to be continued
#here to be continued
@r_admin.message(StateFilter(FsmAdmin.add_category),)
async def check_and_write_category(db_instance: BotDB, state: FSMContext, message: Message):
    categories = await db_instance.get_categories()
    if message.text in categories:
        await message.edit_text(MESSAGES['add_category_already_exist'], reply_markup=only_back_menu_markup)
    else:
        await message.edit_text(text="mock", reply_markup=only_back_menu_markup)




# @r_admin.callback_query()
# async def debug_function(call: CallbackQuery):
#     print(call.model_dump_json(indent=4, exclude_none=True))

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