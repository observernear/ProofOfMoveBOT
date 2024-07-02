from aiogram.utils.keyboard import ReplyKeyboardBuilder
import config as cfg

from gresql import db


def location_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text="Получить $POM", request_location=True)
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True)
