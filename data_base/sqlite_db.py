import sqlite3
from datetime import datetime

base = sqlite3.connect('sharaga.db')
cursor = base.cursor()


def sql_start():
    if base:
        print('База данных подключена!')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name_group TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS news (dt DATETIME, title TEXT, content TEXT, img TEXT)')
    base.commit()


async def get_data_from_proxy(state):
    async with state.proxy() as data:
        return data


async def add_news(state):
    proxy_data = await get_data_from_proxy(state)
    cursor.execute('INSERT INTO news VALUES (?, ?, ?, ?)', (datetime.now(),) + tuple(proxy_data.values()))
    base.commit()


async def get_news():
    return [n for n in cursor.execute('SELECT * FROM news')]


async def delete_news(date):
    datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    cursor.execute('DELETE FROM news WHERE dt = ?', (datetime_obj,))
    base.commit()

