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
    SUGAR = ["正常甜","不要太甜","少糖","半糖","微糖","無糖"]
    ICE = ["正常冰","少冰","微冰","去冰","常溫","熱"]
    BRAND = "五十嵐"
    START_TIME = [0, 0]
    END_TIME = [0, 1]
    AM_PM = "pm"
    TODAY_ORDERS = {'TodayOrder': []} 