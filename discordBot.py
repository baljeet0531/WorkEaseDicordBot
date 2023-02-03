from dataclasses import dataclass
from config import Config, bot
from botEndpoint import *

@bot.event
async def on_ready():
    print("Hello!! I'm botender!!")
    channel = bot.get_channel(Config.CHANNEL_ID)
    await channel.send("Hello!! I'm botender!!")

bot.run(Config.BOT_TOKEN)