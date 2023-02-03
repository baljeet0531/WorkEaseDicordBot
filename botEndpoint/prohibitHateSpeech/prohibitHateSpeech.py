from discord.ext import commands, tasks
from dataclasses import dataclass
from config import Config
from config import bot
import discord
import re

hate_word = {"爛", "幹", "糙", "媽的", "幹*娘", "腦殘"}

# Overriding the default provided on_message forbids any extra commands from running.
@bot.event
async def on_message(message):
    
    if message:
        hatter = [True for hw in hate_word if re.search(re.escape(hw), message.content)]
        if any(hatter):
            await message.channel.send("請您注意言論, 禁止使用不雅字詞")

    await bot.process_commands(message)