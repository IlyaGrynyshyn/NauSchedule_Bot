from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Для початку спілкування з ботом",
            "/help - Допомога по командам бота",
            '/about - Інформація про бота')

    
    await message.answer("\n".join(text))
