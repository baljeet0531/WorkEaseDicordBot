import discord
from config import bot

@bot.tree.command(name="show_menu")
async def show_menu(interaction: discord.Interaction):
    file = discord.File("img/50嵐.jpg")
    await interaction.response.send_message(file=file)