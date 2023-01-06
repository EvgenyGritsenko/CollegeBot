from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base.sqlite_db import get_all_questions
from create_bot import bot, ADMINS_CHAT_ID
from handlers import states


def create_delete_news_keyboard(date):
    kb = InlineKeyboardMarkup()
    btn_delete = InlineKeyboardButton('Удалить новость', callback_data=f'news {date}')
    kb.add(btn_delete)
    return kb


async def create_reply_keyboard(user_id):
    kb = InlineKeyboardMarkup()
    reply = InlineKeyboardButton('Ответить',
                                 callback_data=f'qtn {user_id}')
    kb.add(reply)
    return kb
