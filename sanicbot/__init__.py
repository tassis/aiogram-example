from urllib.parse import urljoin
from sanic import Sanic, Request, response
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentTypes, Update

from . import config

# define sanic application.
app = Sanic(__name__)
app.update_config(config)

# define Aiogram instance
bot = Bot(app.config["BOT_TOKEN"])
dp = Dispatcher(bot)


# initialize project
@app.main_process_start
async def main_startup(app: Sanic):
    # register webhook url4 ex: https://domain.com/webhook
    WEBHOOK_ROUTE = app.config["WEBHOOK_ROUTE"]
    DOMAIN_URL = app.config["DOMAIN_URL"]
    WEBHOOK_URL = urljoin(DOMAIN_URL, WEBHOOK_ROUTE)
    print(WEBHOOK_URL)
    await bot.set_webhook(WEBHOOK_URL)


# define bot message handler.
@dp.message_handler(content_types=ContentTypes.ANY)
async def on_message(message: Message):
    print(message)



# define sanic route to revice webhook message.
@app.post("/webhook")
async def on_update(request: Request):
    _update = Update(**request.json)
    await dp.process_update(_update)
    return response.empty(status=200)