from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


storage = MemoryStorage()

bot = Bot(token='5444138196:AAHr0gHl7khtZsLYMCh76hKSUfpDv07bjP0')
ADMINS_CHAT_ID = -817203032

dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
