#might make a tut on how to add commands
import discord
import requests
import asyncio

TOKEN1 = "Nzc2MDQ5MzMxNjI3MDk4MTQz.X9g9kQ.gqOtml38QCN09pIw9Mjb5mJvb-Y"

TOKEN2 = "Nzg4Mzg3ODA4MDAzMDk2NjE2.X9iyBQ.17MOssymUiG45c5wKA6GmA6B2YM"

TOKEN3 = "Nzc2MDQ1MzE0MzIyNTk1ODYw.X9hHGQ.e1Pd1nh5OHzdNNAVjUGEsIJ44fI"

TOKEN4 = "Nzg4Mzg5MDA0NDkxODgyNDk2.X9iy0g.pfnvYZApPlNjK0MiixOV69QEX4c"

TOKEN5 = "Nzg4Mzg5NTc4NTQwNTgwODg0.X9mAWA.bqhyOutHaXHJ2Pn8c_c2SW8KSiY"

TOKEN6 = "Nzg4NjEwNjU1MzY4MTE4MzAy.X9mBag.4msMuuru0kFw1jcQLokHTiLDnf0"

TOKEN7 = "Nzg4NjEzODEyNjk3MzAxMDEy.X9mEfQ.vCY6vl9HJ95zrjc9op4-jvMz-Nw"

TOKEN8 = "Nzg4NjE0ODE3MzA4MjEzMjY5.X9mHgQ.67Q25A9454SPNlKNTl-toLu9chY"

client1 = discord.Client(self_bot = True)

client2 = discord.Client(self_bot = True)

client3 = discord.Client(self_bot = True)

client4 = discord.Client(self_bot = True)

client5 = discord.Client(self_bot = True)

client6 = discord.Client(self_bot = True)

client7 = discord.Client(self_bot = True)

client8 = discord.Client(self_bot = True)


@client1.event
async def on_ready():
   print(f"Bot 1 is ready!!. Login as {client1.user.name}")
   
@client2.event
async def on_ready():
   requests.post("https://discordapp.com/api/v6/invites/gkZmcu4gWq",headers={'authorization':TOKEN2})
   print(f"Bot 2 is ready!!. Login as {client2.user.name}")

@client3.event
async def on_ready():
   print(f"Bot 3 is ready!!. Login as {client3.user.name}")

@client4.event
async def on_ready():
   requests.post("https://discordapp.com/api/v6/invites/gkZmcu4gWq",headers={'authorization':TOKEN4})
   print(f"Bot 4 is ready!!. Login as {client4.user.name}")

@client5.event
async def on_ready():
   requests.post("https://discordapp.com/api/v6/invites/gkZmcu4gWq",headers={'authorization':TOKEN5})
   print(f"Bot 1 is ready!!. Login as {client1.user.name}")
   
@client6.event
async def on_ready():
   requests.post("https://discordapp.com/api/v6/invites/gkZmcu4gWq",headers={'authorization':TOKEN6})
   print(f"Bot 2 is ready!!. Login as {client2.user.name}")

@client7.event
async def on_ready():
   requests.post("https://discordapp.com/api/v6/invites/gkZmcu4gWq",headers={'authorization':TOKEN7})
   print(f"Bot 3 is ready!!. Login as {client3.user.name}")

@client8.event
async def on_ready():
   requests.post("https://discordapp.com/api/v6/invites/gkZmcu4gWq",headers={'authorization':TOKEN8})
   print(f"Bot 4 is ready!!. Login as {client4.user.name}")

loop = asyncio.get_event_loop()
loop.create_task(client1.start(TOKEN1, bot=False))
loop.create_task(client2.start(TOKEN2, bot=False))
loop.create_task(client3.start(TOKEN3, bot=False))
loop.create_task(client4.start(TOKEN4, bot=False))

loop.create_task(client5.start(TOKEN5, bot=False))
loop.create_task(client6.start(TOKEN6, bot=False))
loop.create_task(client7.start(TOKEN7, bot=False))
loop.create_task(client8.start(TOKEN8, bot=False))

loop.run_forever()
