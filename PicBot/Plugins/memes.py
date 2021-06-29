from pyrogram import Client, filters
import requests
import re

@Client.on_message(filters.command(["meme"]))
async def meme(bot, update):
    hmm_s = "https://some-random-api.ml/meme"
    r = requests.get(url=hmm_s).json()
    image_s = r["image"]
    await bot.send_photo(message.chat.id, image_s)
