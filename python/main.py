import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from keep_alive import keep_alive

bot = Bot(token='5998411395:AAGd5hnfCzVexY1F0Ryy5XH862fSfflvPdg')
dp = Dispatcher(bot)
openai.api_key = "sk-proj-dku33dCFA4CRNwVUkjRsT3BlbkFJfZWrgeJenYTzNSiNo2Xn"

keep_alive()

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! I'm GPT chat bot, Ask me something")

@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await message.reply(response.choices[0].text)

if __name__ == "__main__":
    executor.start_polling(dp)
      
