from pyrogram import Client, filters 


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    me = client.me.first_name
    await bot.send_message(
        chat_id=update.chat.id,
        text=f"__Hello {me}!\nI'm Picbot\nCheck__ /help __to know how to use me\n**My Owner:** [Naveen](t.me/Sniper_xd)",
        reply_to_message_id=update.message_id
    )
