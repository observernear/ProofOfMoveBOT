from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo
import config as cfg

from gresql import db


def main_menu_inline_keyboard(id):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Поехали", web_app=WebAppInfo(url=f"https://0d98-46-73-19-19.ngrok-free.app/"))
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()
