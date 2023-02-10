from config import bot, Config
import discord

@bot.tree.command(name="show_drink_orders")
async def show_drink_orders(interaction: discord.Interaction):
    
    users = Config.TODAY_ORDERS
    # await interaction.response.send_message(users)

    # print(users.get('1068452639714578452'))
    # print(len(users[0]['item']))
    num = len(users["TodayOrder"])
    print("Number", num)

    order = []
    for i in range(0, num):
        name = users["TodayOrder"][i]["Name"]
        item = users["TodayOrder"][i]["item"]
        sugar = users["TodayOrder"][i]["Sugar"]
        ice = users["TodayOrder"][i]["ice"]
        order.append(name+item+sugar+ice)
    # print("\n".join('%s' % id for id in order))
    # print(" ".join(order)
    # interaction.followup.send(" ".join(results.get("Name")+results.get("a1")+results.get("a2")+results.get("a3")))
    await interaction.response.send_message("\n".join('%s' % id for id in order))