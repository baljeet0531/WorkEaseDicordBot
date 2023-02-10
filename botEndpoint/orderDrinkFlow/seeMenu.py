from config import bot
import discord
from datetime import datetime
from .chooseDrink import chooseDrink
from config import Config

async def menu(interaction: discord.Interaction, name, End_hour, End_min):
    file = discord.File("img/50嵐.jpg")
    await interaction.response.send_message(file=file)
    await chooseDrink(interaction, name, End_hour, End_min)

@bot.tree.command(name="order_drinks")
async def see_menu(interaction: discord.Interaction, 名稱: str):
    name = [名稱]
    now_hour = datetime.now().strftime('%H')
    now_min = datetime.now().strftime('%M')

    End_hour = Config.END_TIME[0]
    End_min = Config.END_TIME[1]
    Start_hours = int(now_hour)
    Start_min = int(now_min)
    if End_hour < Start_hours:
        await interaction.response.send_message("---點單時間已截止---")
        return
    elif End_hour == Start_hours and End_min <= Start_min:
        await interaction.response.send_message("---點單時間已截止---")
        return
    else:
        await menu(interaction, name, End_hour, End_min)