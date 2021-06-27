from pyrogram import Client, filters


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    me = client.me.first_name
    text=f"__Hello {me}!\nI'm Picturebot\nCheck__/help__ to get available commands"
    mypic="https://telegra.ph//file/894df85d26b8b72f0745b.jpg"
    await bot.send_photo(
            message.chat.id,
            mypic,
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Dev", url="t.me/Sniper_xd")]]
            ),
        )
