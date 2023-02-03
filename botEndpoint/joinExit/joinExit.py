from discord.ext import commands, tasks
from dataclasses import dataclass
from config import Config
from config import bot

@bot.event
async def on_member_join(member):
    join_msg = member + ", Welcome to this server... Say HI to your homie here!!"
    channel = bot.get_channel(Config.CHANNEL_ID)
    await channel.send(join_msg)


@bot.event
async def on_member_remove(member):
    exit_msg = member + " has left here... Plz pray for him/her"
    channel = bot.get_channel(Config.CHANNEL_ID)
    await channel.send(exit_msg)