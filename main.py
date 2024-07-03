from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import BotCommand
from aiogram.client.bot import DefaultBotProperties

import logging
import contextlib
import asyncio

import config as cfg
from handlers.commands import *
from handlers.messages import *
from handlers.callback import *
from handlers.location import *


async def start():

    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    bot: Bot = Bot(token=cfg.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    dp.message.register(start_command, Command(commands=["start"]))
    dp.message.register(location_handler, F.location)
    dp.callback_query.register(callback_handler_profile, F.data.in_(["info", "location"]))

    bot_commands = [
        BotCommand(command="/start", description="Запуск")
    ]

    await bot.set_my_commands(bot_commands)
    await bot.set_my_description(description='Запуск бота')
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
