#might make a tut on how to add commands
import discord

import asyncio

TOKEN1 = "Nzc2MDQ5MzMxNjI3MDk4MTQz.X9g9kQ.gqOtml38QCN09pIw9Mjb5mJvb-Y"

TOKEN2 = "Nzg4Mzg3ODA4MDAzMDk2NjE2.X9iyBQ.17MOssymUiG45c5wKA6GmA6B2YM"

TOKEN3 = "Nzc2MDQ1MzE0MzIyNTk1ODYw.X9hHGQ.e1Pd1nh5OHzdNNAVjUGEsIJ44fI"

TOKEN4 = "Nzg4Mzg5MDA0NDkxODgyNDk2.X9iy0g.pfnvYZApPlNjK0MiixOV69QEX4c"

client1 = discord.Client(self_bot = True)

client2 = discord.Client(self_bot = True)

client3 = discord.Client(self_bot = True)

client4 = discord.Client(self_bot = True)

@client1.event
async def on_ready():
   print("Bot 1 is ready!!")

@client2.event
async def on_ready():
   print("Bot 2 is ready!!")

@client3.event
async def on_ready():
   print("Bot 3 is ready!!")

@client4.event
async def on_ready():
   print("Bot 4 is ready!!")

loop = asyncio.get_event_loop()
loop.create_task(client1.start(TOKEN1, bot=False))
loop.create_task(client2.start(TOKEN2, bot=False))
loop.create_task(client3.start(TOKEN3, bot=False))
loop.create_task(client4.start(TOKEN4, bot=False))
loop.run_forever()
