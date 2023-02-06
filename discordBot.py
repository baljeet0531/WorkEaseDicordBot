from dataclasses import dataclass
from config import Config, bot
from botEndpoint import *
from loguru import logger
from model import User_info
from db import get_session
from loguru import logger

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    channel = bot.get_channel(Config.CHANNEL_ID)
    await channel.send("Hola~ Bot is online now!!")

bot.run(Config.BOT_TOKEN)