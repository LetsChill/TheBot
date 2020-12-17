#might make a tut on how to add commands
import discord
import requests
import asyncio

from discord.utils import get

#TOKEN HOLDER!!!

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

TOKEN11 = "Nzg4NjM5NjY5MTQyNDIxNTA1.X9opIQ.FqvDOrtrcWycGvIxDSwUoeFZ42Q"

TOKEN12 = "Nzg4NzkxNzI2NjE3MjY0MTQ4.X9oqDA.3YlyX0JlSAyqljlkkX0pe98UoxU"

TOKEN13 = "Nzg4NzkyNzM3NTU3MzgxMTgy.X9oqxA.T66Mbcw1qVagvAjDQWyT6-W-VgA"

TOKEN14 = "Nzg4NzkzMzQ0MzY1MDM1NTUw.X9orcQ.icxvipPgHSgTo2HYNcMF8OQqCtA"

TOKEN15 = "Nzg4Nzk0NDQ3Mzc0MTg4NTc1.X9osvQ.bncVRtfIqr6HoDdlOlyGHNn-9NI"

#JOINER, LEAVER!!!

TARGET = "https://discordapp.com/api/v6/invites/nhXWuQdd"

LEAVE = 784444505625329704

#CLIENT DECLARES

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

client11 = discord.Client(self_bot = True)

client12 = discord.Client(self_bot = True)

client13 = discord.Client(self_bot = True)

client14 = discord.Client(self_bot = True)

client15 = discord.Client(self_bot = True)

#CLIENT SCRIPTS!!!

@client1.event
async def on_ready():
   SERVER = client1.get_guild(LEAVE)
   await client1.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN1})
   await SERVER.leave()
   print(f"Bot 1 is ready!!. Login as {client1.user.name}")
   
@client2.event
async def on_ready():
   SERVER = client2.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN2})
   await SERVER.leave()
   print(f"Bot 2 is ready!!. Login as {client2.user.name}")

@client3.event
async def on_ready():
   SERVER = client3.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN3})
   await SERVER.leave()
   print(f"Bot 3 is ready!!. Login as {client3.user.name}")

@client4.event
async def on_ready():
   SERVER = client4.get_guild(LEAVE)
   await client1.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN4})
   await SERVER.leave()
   print(f"Bot 4 is ready!!. Login as {client4.user.name}")

@client5.event
async def on_ready():
   SERVER = client5.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN5})
   #await SERVER.leave()
   print(f"Bot 5 is ready!!. Login as {client5.user.name}")
   
@client6.event
async def on_ready():
   SERVER = client6.get_guild(LEAVE)
   await client1.change_presence(status=discord.Status.dnd)
   requests.post(TARGET,headers={'authorization':TOKEN6})
   await SERVER.leave()
   print(f"Bot 6 is ready!!. Login as {client6.user.name}")

@client7.event
async def on_ready():
   SERVER = client7.get_guild(LEAVE)
   await client1.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN7})
   await SERVER.leave()
   print(f"Bot 7 is ready!!. Login as {client7.user.name}")

@client8.event
async def on_ready():
   SERVER = client8.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN8})
   await SERVER.leave()
   print(f"Bot 8 is ready!!. Login as {client8.user.name}")

@client9.event
async def on_ready():
   SERVER = client9.get_guild(LEAVE)
   await client1.change_presence(status=discord.Status.dnd)
   requests.post(TARGET,headers={'authorization':TOKEN9})
   await SERVER.leave()
   print(f"Bot 9 is ready!!. Login as {client9.user.name}")

@clientX.event
async def on_ready():
   SERVER = clientX.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKENX})
   await SERVER.leave()
   print(f"Bot X is ready!!. Login as {clientX.user.name}")

@client11.event
async def on_ready():
   SERVER = client11.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN11})
   await SERVER.leave()
   print(f"Bot 11 is ready!!. Login as {client11.user.name}")

@client12.event
async def on_ready():
   SERVER = client12.get_guild(LEAVE)
   await client1.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN12})
   await SERVER.leave()
   print(f"Bot 12 is ready!!. Login as {client12.user.name}")

@client13.event
async def on_ready():
   SERVER = client13.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN13})
   await SERVER.leave()
   print(f"Bot 13 is ready!!. Login as {client13.user.name}")

@client14.event
async def on_ready():
   SERVER = client14.get_guild(LEAVE)
   await client1.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN14})
   await SERVER.leave()
   print(f"Bot 14 is ready!!. Login as {client14.user.name}")

@client15.event
async def on_ready():
   SERVER = client15.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN15})
   await SERVER.leave()
   print(f"Bot 15 is ready!!. Login as {client15.user.name}")

#LOOP FUNCTIONS!!!

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

loop.create_task(client11.start(TOKEN11, bot=False))
loop.create_task(client12.start(TOKEN12, bot=False))
loop.create_task(client13.start(TOKEN13, bot=False))
loop.create_task(client14.start(TOKEN14, bot=False))
loop.create_task(client15.start(TOKEN15, bot=False))

loop.run_forever()
