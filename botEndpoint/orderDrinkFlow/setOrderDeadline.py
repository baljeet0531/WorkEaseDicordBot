from config import bot, Config
from datetime import datetime
import discord

@bot.tree.command(name="set_deadline")
async def set_deadline(interaction: discord.Interaction, am_pm: str, hour: int, min: int):

    now_hour = datetime.now().strftime('%H')
    now_min = datetime.now().strftime('%M')
    await interaction.response.send_message("現在時間 " + now_hour + ":" + now_min)
   # await interaction.followup.send(now_time)

    print(hour, min)
    if am_pm == "pm":
        hour += 12
    elif am_pm == "am":
        pass
    else:
        await interaction.followup.send("請輸入正確格式! ")
        return

    if hour < 0 or hour > 24:
        await interaction.followup.send("請輸入正確格式! ")
        return
    elif min < 0 or min >= 60:
        await interaction.followup.send("請輸入正確格式! ")
        return
    else:
        pass

    Config.AM_PM = am_pm
    Config.END_TIME[0] = hour
    Config.END_TIME[1] = min

    show_min = min
    if min == 0:
        show_min = '00'
    else:
        show_min = str(min)
    await interaction.followup.send("您設定的截止時間為:  " + str(am_pm) + " "+str(hour) + ":" + show_min)
