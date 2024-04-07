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


class Reference:
    def __init__(self) -> None:
        self.response = ""

reference = Reference()

def clear_past():
    reference.response = ""

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This handler clears the conversation
    """
    clear_past()
    await message.reply("I have cleared the conversation and context")  

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """This handler receives message with 'start' or 'help' commands
    
    Args:
         message (types.Message): _description_
    """
    await message.reply("Hi! \n I am a Chat Bot! Created By Pravin \n How can i assist you?") 

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """This handler displays help commands
    """
    help_command = """
    Hi There, I am a Bot created by Pravin! Please follow these commands-
    /start - to start the conversation
    /clear - to clear the past conversation
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)     
               
@dispatcher.message_handler()
async def main_bot(message: types.Message):
    """
    This handler process the user's input and generate the response using the openai API
    
    """
    print(f">>>USER: \n \t{message.text}")
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages = [
            {"role" : "assistant", "content" : reference.response}, ##role assistant
            {"role" : "user" , "content" : message.text} ## our query
        ])
    reference.response = response['choices'][0]['message']['content']
    print(f">>>chatGPT: \n \t{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)



if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)    