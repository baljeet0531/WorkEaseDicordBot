from discord.ext import commands, tasks
from dataclasses import dataclass
import datetime
import discord
from config import Config
from config import bot

@dataclass
class Session:
    is_active : bool = False
    start_time : int = 0

session=  Session()

@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")

    break_reminder.start()
    await ctx.send(f"New session started at {human_readable_time}")

@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("A session is already deactive!")
        return
    
    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_time = str(datetime.timedelta(seconds = duration))
    await ctx.send(f"Session last for {human_readable_time} seconds")

@tasks.loop(minutes = Config.MAX_SESSION_MINUTES, count = 2)
async def break_reminder():

    # Igonring the first execution
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(Config.CHANNEL_ID)

    break_reminder.stop()
    await channel.send(f"**Take a break!**\nYou've been studying for {Config.MAX_SESSION_MINUTES}")