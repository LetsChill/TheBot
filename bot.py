#might make a tut on how to add commands
import discord
import requests
import asyncio

from discord.utils import get

TOKEN1 = "Nzc2MDQ5MzMxNjI3MDk4MTQz.X9g9kQ.gqOtml38QCN09pIw9Mjb5mJvb-Y"

TOKEN2 = "Nzg4Mzg3ODA4MDAzMDk2NjE2.X9iyBQ.17MOssymUiG45c5wKA6GmA6B2YM"

TOKEN3 = "Nzc2MDQ1MzE0MzIyNTk1ODYw.X9hHGQ.e1Pd1nh5OHzdNNAVjUGEsIJ44fI"

TOKEN4 = "Nzg4Mzg5MDA0NDkxODgyNDk2.X9iy0g.pfnvYZApPlNjK0MiixOV69QEX4c"

TOKEN5 = "Nzg4Mzg5NTc4NTQwNTgwODg0.X9mAWA.bqhyOutHaXHJ2Pn8c_c2SW8KSiY"

TOKEN6 = "Nzg4NjEwNjU1MzY4MTE4MzAy.X9mBag.4msMuuru0kFw1jcQLokHTiLDnf0"

TOKEN7 = "Nzg4NjEzODEyNjk3MzAxMDEy.X9mEfQ.vCY6vl9HJ95zrjc9op4-jvMz-Nw"

TOKEN8 = "Nzg4NjE0ODE3MzA4MjEzMjY5.X9mHgQ.67Q25A9454SPNlKNTl-toLu9chY"

TOKEN9 = "Nzg4NjI5MTU4MTYyMDcxNTU0.X9mSbw.oaIdAsZjarHBeu1ipyivwnfWgUY"

TOKENX = "Nzg4NjMwNTkwNzYwMDI2MTYy.X9mUTA.zcEYkwRou8gxPJyXkOIxliXcssg"

TARGET = "https://discordapp.com/api/v6/invites/tzf2bV3SmC"

LEAVE = "742618169419628554"

client1 = discord.Client(self_bot = True)

client2 = discord.Client(self_bot = True)

client3 = discord.Client(self_bot = True)

client4 = discord.Client(self_bot = True)

client5 = discord.Client(self_bot = True)

client6 = discord.Client(self_bot = True)

client7 = discord.Client(self_bot = True)

client8 = discord.Client(self_bot = True)

client9 = discord.Client(self_bot = True)

clientX = discord.Client(self_bot = True)

@client1.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN1})
   await client1.get_guild(LEAVE).leave()
   print(f"Bot 1 is ready!!. Login as {client1.user.name}")
   
@client2.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN2})
   await client2.get_guild(LEAVE).leave()
   print(f"Bot 2 is ready!!. Login as {client2.user.name}")

@client3.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN3})
   await client3.get_guild(LEAVE).leave()
   print(f"Bot 3 is ready!!. Login as {client3.user.name}")

@client4.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN4})
   await client4.get_guild(LEAVE).leave()
   print(f"Bot 4 is ready!!. Login as {client4.user.name}")

@client5.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN5})
   await client5.get_guild(LEAVE).leave()
   print(f"Bot 5 is ready!!. Login as {client5.user.name}")
   
@client6.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN6})
   await client6.get_guild(LEAVE).leave()
   print(f"Bot 6 is ready!!. Login as {client6.user.name}")

@client7.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN7})
   await client7.get_guild(LEAVE).leave()
   print(f"Bot 7 is ready!!. Login as {client7.user.name}")

@client8.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN8})
   await client8.get_guild(LEAVE).leave()
   print(f"Bot 8 is ready!!. Login as {client8.user.name}")

@client9.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKEN9})
   await client9.get_guild(LEAVE).leave()
   print(f"Bot 9 is ready!!. Login as {client9.user.name}")

@clientX.event
async def on_ready():
   requests.post(TARGET,headers={'authorization':TOKENX})
   await clientX.get_guild(LEAVE).leave()
   print(f"Bot X is ready!!. Login as {clientX.user.name}")

loop = asyncio.get_event_loop()
loop.create_task(client1.start(TOKEN1, bot=False))
loop.create_task(client2.start(TOKEN2, bot=False))
loop.create_task(client3.start(TOKEN3, bot=False))
loop.create_task(client4.start(TOKEN4, bot=False))

loop.create_task(client5.start(TOKEN5, bot=False))
loop.create_task(client6.start(TOKEN6, bot=False))
loop.create_task(client7.start(TOKEN7, bot=False))
loop.create_task(client8.start(TOKEN8, bot=False))

loop.create_task(client9.start(TOKEN9, bot=False))
loop.create_task(clientX.start(TOKENX, bot=False))

loop.run_forever()
