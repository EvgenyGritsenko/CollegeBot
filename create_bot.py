from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


storage = MemoryStorage()

bot = Bot(token='5444138196:AAFU60c5xSvIeaf6TPQ37mA4bKe7pA5PwKk')

dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
