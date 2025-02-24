 # commands.py
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.dispatcher.router import Router

router = Router()

# ОБРАБОТЧКИ
async def command_start(message: types.Message):
    await message.answer("👋 Привет! Я бот, мой создатель не наделил меня никакими полезными функциям, потому что я всего лишь пример для аннотированного алгоритма, что бы это не означало 😥")

# Регистрация обработчиков
def register_handlers(dp):
    # Регистрация команд
    router.message.register(command_start, CommandStart())

    dp.include_router(router)