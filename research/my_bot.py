from aiogram import Bot, Dispatcher,executor,types
from dotenv import load_dotenv
import logging 
import os
import openai

load_dotenv()

API_TOKEN = os.getenv("OPENAI_API_KEY")
TOKEN = os.getenv("TOKEN")


##Connect with OpenAI
openai.api_key = API_TOKEN

MODEL_NAME = "gpt-3.5-turbo"

## Initialize Bot
bot = Bot(token= TOKEN)
dispatcher = Dispatcher(bot)

