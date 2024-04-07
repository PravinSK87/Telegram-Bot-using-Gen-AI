from aiogram import Bot, Dispatcher,types, executor
from dotenv import load_dotenv
import logging
import os

load_dotenv()

API_TOKEN = os.getenv("TOKEN")

##Configure Logging
logging.basicConfig(level=logging.INFO)

##Initialize Bot
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """This handler receives message with 'start' or 'help' commands
    
    Args:
         message (types.Message): _description_
    """
    await message.reply("Hi! \n I am echo bot!\n Powered by Aiogram")    

@dp.message_handler()
async def echo(message: types.Message):
    """This will return echo message
    
    Args:
         message (types.Message): _description_
    """
    await message.reply(message.text) 



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)    