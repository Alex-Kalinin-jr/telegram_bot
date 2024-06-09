from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.utils import get_language
from data.button_name import kb_main_menu
from aiogram.filters.callback_data import CallbackData

BUTTONS_DICT = get_language()


b_main_menu = InlineKeyboardButton(text=BUTTONS_DICT['main_menu'], callback_data='main_menu')
b_back = InlineKeyboardButton(text=BUTTONS_DICT['back'], callback_data='back')


class MyCallbackFactory(CallbackData, prefix="my_cb"):
    action: str
    item_id: str


def get_price_list_kb(items: dict) -> ReplyKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for item in items:
        keyboard.row(
            InlineKeyboardButton(text=item, callback_data=items[item]),
            InlineKeyboardButton(text=BUTTONS_DICT['get_infro'],
                                 callback_data=MyCallbackFactory(action="get_info", item_id=items[item]).pack()
                                 ))
        
    keyboard.row(b_back)

    return keyboard.as_markup(resize_keyboard=True)


def get_positions_kb(items: dict) -> ReplyKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for item in items:
        keyboard.row(InlineKeyboardButton(text=item, callback_data=items[item]))
        
    keyboard.row(b_back)

    return keyboard.as_markup(resize_keyboard=True)


def get_keyboard(keyboards: dict) -> ReplyKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    
    for button in keyboards:
        keyboard_builder.row(InlineKeyboardButton(text=BUTTONS_DICT[button], callback_data=button))
        
    return keyboard_builder.as_markup(resize_keyboard=True)