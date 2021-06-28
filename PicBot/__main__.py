import logging
import os
import platform

import pyrogram
from pyrogram import __version__


async def load_plugins():
   """Load modules"""
   logging.info("Loading [Modules]")
   await run_cmd("bash PicBot/Plugins.sh")
   xtra_mods = plugin_collecter("./PicBot/Plugins")
   for mods in xtra_mods:
        try:
            load_xtra_mod(mods)
        except Exception as e:
            logging.error(
                "[BOR][PLUGINS] - Failed To Load : " + f"{mods} - {str(e)}"
            )
   info = f"""PicBot is based on pyrogram V{__version__}
Python Version : {platform.python_version()}
Picbot Version : 1.0   

logging.info(info)
    await pyrogram.idle()


if __name__ == "__main__":
    app.loop.run_until_complete(run_bot())
