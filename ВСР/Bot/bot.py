from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not API_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN provided")

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)