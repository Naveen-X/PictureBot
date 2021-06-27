from pyrogram import Client, filters
import requests

        
@Client.on_message(filters.command(["panda"]))
async def panda(bot, update):
    link = "https://some-random-api.ml/img/panda"
    r = requests.get(url=link).json()
    image_s = r["image"]
    await bot.send_photo(image_s)