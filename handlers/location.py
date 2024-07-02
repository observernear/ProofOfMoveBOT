from aiogram import Bot
from aiogram.types import Message
import requests
from keyboards.inline import *


async def location_handler(message: Message, bot: Bot):
    lat = message.location.latitude
    lon = message.location.longitude
    resp = requests.post('https://proofofmove.ru/api/ClaimReward', json={"tg_id": message.from_user.id, "location": f"{lat} {lon}"})
    tokens = resp.json()['tokens']
    if tokens == 0:
        await bot.send_message(chat_id=message.chat.id, text="Еще рано, более точное время можно посмотреть в игре", reply_markup=only_game_inline_keyboard())
        return
    await bot.send_message(chat_id=message.chat.id, text=f"Вы получили {tokens} $POM", reply_markup=only_game_inline_keyboard())