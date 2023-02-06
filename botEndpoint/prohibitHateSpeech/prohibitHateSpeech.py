from discord.ext import commands, tasks
from dataclasses import dataclass
from config import Config
from config import bot
import discord
import re

# Overriding the default provided on_message forbids any extra commands from running.
@bot.event
async def on_message(message : discord.message.Message):
    
    if message and message.author.id != bot.user.id :
        hatter = [True for hw in Config.HATE_WORD if re.search(re.escape(hw), message.content)]
        if any(hatter):
            await message.channel.send("請您注意言論, 禁止使用不雅字詞")

    await bot.process_commands(message)