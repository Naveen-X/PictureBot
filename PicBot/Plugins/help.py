from pyrogram import Client, filters

@Client.on_message(filters.command(["help"]))
async def help_menu(bot, update):
     text = f"Heya!\nTheese are the available commands right now\n\n/dog - sends a random dog image\n/cat - sends a random cat image\n/panda - sends a random panda image\n/meme - sends a random meme"
     await bot.send_message(message, text)
