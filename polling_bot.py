from aiogram import Bot
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling

BOT_TOKEN = "5442570310:AAHR_lkUB_7SlCOJZSarR6QU9OS_kXICn-c"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# Process start command
@dp.message_handler(commands=['start'])
async def on_start_command():  
    print("on start command")

# Process all messages except start command
@dp.message_handler(content_types=ContentTypes.ANY)
async def on_message(message: Message):
    await message.reply(message.from_user.id)

async def on_startup(dispatcher: Dispatcher):
    print("startup")

async def on_shutdown(dispatcher: Dispatcher):
    print("shutdown")


if __name__ == "__main__":
    start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)

