import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
import discord

load_dotenv()

bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "1"))
    MAX_SESSION_MINUTES = int(os.environ.get("MAX_SESSION_MINUTES", "1"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    HATE_WORD = os.environ.get("HATE_WORD", [])
    DIRECTOR_ID = os.environ.get("DIRECTOR_ID", 0)