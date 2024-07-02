from aiogram import Bot
from aiogram.types import CallbackQuery, InputMediaDocument
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext
from random import randint
from datetime import datetime
import os

from keyboards.inline import *
from keyboards.reply import *
from gresql import db
import config as cfg
from fsm.state import *



async def callback_handler_profile(callback: CallbackQuery, bot: Bot, state: FSMContext):
    if callback.data == "location":
        await bot.send_message(chat_id=callback.from_user.id, text='Данная функция создана для тех у кого устройство не поддерживает отправку геолокации внутри игры.\n\n<b>Вы можете отправить свою локацию сюда, просто нажмите на кнопку <i>"Получить $POM"</i>, она находиться снизу, где расположена ваша клавиатура</b>\n\n<i>ДАННЫЕ О ВАШЕЙ ГЕОЛОКАЦИИ ОСТАЮТСЯ В СЕКРЕТЕ И НЕ БУДУТ СОХРАНЕНЫ И ИСПОЛЬЗОВАНЫ!</i>', reply_markup=location_reply_keyboard())
