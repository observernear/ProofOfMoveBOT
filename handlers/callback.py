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
    pass
