from discord.ext import commands, tasks
from dataclasses import dataclass
from config import Config
from config import bot
from model import User_info
from db import get_session
from loguru import logger


@bot.event
async def on_member_join(member):

    session = get_session()
    user = session.query(User_info).filter(User_info.name == member.name).first()

    if not user:
        try:
            new_user = User_info(
                    name = member.name,
                    user_id = member.id,
                    points = 0,
                )
            session.add(new_user)
            session.commit()
        except Exception as e:
            logger.warning("Session commit error")

        join_msg = member.name + ", Welcome to this server... Say HI to your homie here!!"
        channel = bot.get_channel(Config.CHANNEL_ID)
        await channel.send(join_msg)


@bot.event
async def on_member_remove(member):

    session = get_session()
    user = session.query(User_info).filter(User_info.name == member.name).first()
    
    if user:
        try:
            session.delete(user)
            session.commit()
        except Exception as e:
            logger.warning("Session commit error")

        exit_msg = member.name + " has left here... Plz pray for him/her"
        channel = bot.get_channel(Config.CHANNEL_ID)
        await channel.send(exit_msg)