from pyrogram import Client, filters
import requests
import re
from bs4 import BeautifulSoup

        
@Client.on_message(filters.command(["panda"]))
async def panda(bot, update):
    link = "https://some-random-api.ml/img/panda"
    r = requests.get(url=link).json()
    image_s = r["image"]
    await bot.send_photo(image_s)


@Client.on_message(filters.command(["cat"]))
async def cat(bot, update):
    link = "https://some-random-api.ml/img/cat"
    r = requests.get(url=link).json()
    image_s = r["image"]
    await bot.send_photo(image_s)


@Client.on_message(filters.command(["dog"]))
async def dog(bot, update):
    link = "https://some-random-api.ml/img/dog"
    r = requests.get(url=link).json()
    image_s = r["image"]
    await bot.send_photo(image_s)
