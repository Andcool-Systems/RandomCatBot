import logging
logging.basicConfig(level=logging.INFO)

import requests
from aiogram import Bot, Dispatcher, executor, types
import time
import os
import sys

API_TOKEN = str(sys.argv[1])

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

url = "https://cataas.com/cat"
url_cute = "https://cataas.com/cat/cute"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply("Привет! Я - бот, который отправит тебе случайных котиков по команде\n/cat или /cutecat")


@dp.message_handler(commands=['cat'])
async def send_welcome(message: types.Message):
    r = requests.get(url)
    id1 = message.chat.id
    with open(f"{id1}.jpg", "wb") as f:
        f.write(r.content)
	
    photo = open(f'{id1}.jpg', 'rb')
    await message.reply_photo(photo, "Рандомный котик :)")

    os.remove(f"{id1}.jpg")


@dp.message_handler(commands=['cutecat'])
async def send_welcome(message: types.Message):
    r = requests.get(url_cute)
    id1 = message.chat.id
    with open(f"{id1}.jpg", "wb") as f:
        f.write(r.content)
	
    photo = open(f'{id1}.jpg', 'rb')
    await message.reply_photo(photo, "Рандомный *милый* котик :)", parse_mode="Markdown")

    os.remove(f"{id1}.jpg")
    
if __name__ == '__main__':
	started = True
	while started:
		try:
			executor.start_polling(dp, skip_updates=True)
			started = False
		except Exception:
			started = True
			print("An error has occurred, reboot in 10 seconds")
			time.sleep(10)
			print("rebooting...")
