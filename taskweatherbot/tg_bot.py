import requests
import datetime
from config import bot_token, ow_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Жду название города...")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        req = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={ow_token}&units=metric"
        )
        data = req.json()
        temp = data["main"]["temp"]
        await message.reply(f"Температура: {temp}C°\n")
    except:
        await message.reply("Я не знаю такого города(((")

if __name__ == '__main__':
    executor.start_polling(dp)
