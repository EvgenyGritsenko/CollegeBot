from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


storage = MemoryStorage()

bot = Bot(token='5444138196:AAEjhGuutCPoKQw_e16N5Q38dpWiEUDJSr0')

dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
