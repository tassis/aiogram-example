from aiogram import Bot
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook

BOT_TOKEN = "5442570310:AAHR_lkUB_7SlCOJZSarR6QU9OS_kXICn-c"

# WEBHOOK SETTING
WEBHOOK_DOMAIN = "https://68dc-211-23-21-139.jp.ngrok.io"
WEBHOOK_PATH="/api"
WEBHOOK_URI=f"{WEBHOOK_DOMAIN}{WEBHOOK_PATH}"

# WEBHOST SETTING
WEB_HOST = "0.0.0.0" # or ip
WEB_HOST_PORT = 8000

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
    await bot.set_webhook(WEBHOOK_URI)

async def on_shutdown(dispatcher: Dispatcher):
    print("shutdown")
    await bot.delete_webhook()


if __name__ == "__main__":
    start_webhook(dispatcher=dp, 
                webhook_path=WEBHOOK_PATH,
                on_startup=on_startup,
                on_shutdown=on_shutdown,
                skip_updates=True,
                host=WEB_HOST, 
                port=WEB_HOST_PORT)

