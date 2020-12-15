#might make a tut on how to add commands
import discord

from discord.ext import commands

TOKEN1 = "Nzc2MDQ5MzMxNjI3MDk4MTQz.X9g9kQ.gqOtml38QCN09pIw9Mjb5mJvb-Y"

TOKEN2 = "Nzg4Mzg3ODA4MDAzMDk2NjE2.X9iyBQ.17MOssymUiG45c5wKA6GmA6B2YM"

client1 = commands.Bot("$$$", self_bot = True)

client2 = commands.Bot("&&&", self_bot = True)

@client.event
async def on_ready():
   print("Bot is ready!!")

@client2.event
async def on_ready():
   print("Bot is ready!!")


loop = asyncio.get_event_loop()
loop.create_task(client1.start('TOKEN1', bot=False))
loop.create_task(client2.start('TOKEN2', bot=False))
loop.run_forever()
