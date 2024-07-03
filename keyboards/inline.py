from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo
import config as cfg

from gresql import db


def main_menu_inline_keyboard(id):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Играть в один клик", web_app=WebAppInfo(url=f"https://proofofmove.ru/"))
    keyboard_builder.button(text="Как играть ?", callback_data="info")
    keyboard_builder.button(text="Наш канал", url="https://t.me/proofofmove")
    #keyboard_builder.button(text="Отправить местоположение", callback_data="location")
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def only_game_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Играть в один клик", web_app=WebAppInfo(url=f"https://proofofmove.ru/"))
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()