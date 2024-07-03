from aiogram import Bot, Dispatcher
from aiogram.types import Message, callback_query, InputMediaDocument
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext
from time import sleep
from datetime import datetime
from aiogram.fsm.storage.memory import MemoryStorage, StorageKey

import config as cfg
from gresql import db

from keyboards.reply import *
from keyboards.inline import *
from fsm.state import FSMregistaration


async def start_command(message: Message, state: FSMContext, bot: Bot):
    id_who = message.text.split()[-1]
    await message.delete()
    if not db.user_exists(int(message.from_user.id)):
        db.add_user(int(message.from_user.id), message.from_user.full_name)
    if not db.user_exists_rob(int(message.from_user.id)):
        db.add_user_rob(int(message.from_user.id))
    if not db.user_exists_robReward(int(message.from_user.id)):
        db.add_user_robReward(int(message.from_user.id))
    if not db.user_exists_referral(int(message.from_user.id)):
        if id_who.isdigit() and db.user_exists_referral(int(id_who)):
            db.add_user_referral(int(message.from_user.id), int(id_who))
            db.plus_whom(int(id_who), str(message.from_user.id))
        else:
            db.add_user_referral(int(message.from_user.id))
    await state.clear()
    await bot.send_message(chat_id=message.chat.id, text="<b>Proof Of Move</b>\n\nДобро пожаловать в проект!\nТут ты сможешь зарабатывать криптовалюту за шаги, а также покупать роботов, которые будут ходить и зарабатывать.", reply_markup=main_menu_inline_keyboard(message.from_user.id))