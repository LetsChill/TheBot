#might make a tut on how to add commands
import discord
import requests
import asyncio

from discord.utils import get

#TOKEN HOLDER!!!

TOKEN1 = "Nzc2MDQ5MzMxNjI3MDk4MTQz.X9g9kQ.gqOtml38QCN09pIw9Mjb5mJvb-Y"

TOKEN2 = "Nzg4OTgyMTUzODAzMDcxNTA5.X9uoSA.e5ydIzmuceF5zPXaN4Fnl8v0uZU"

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

TOKEN16 = "Nzg4OTcxMjUxNzIwNzgxODg0.X9rRRw.sK6Cf2tGtHBNSForctu9K8cLpoU"

TOKEN17 = "Nzg4OTcyNTMyNTkzNDU5MjEx.X9rSUg.nAuG8PG-F96lQjWllc1dki7MvXs"

TOKEN18 = "Nzg4OTczMjcxMDA1MDAzODE2.X9rS7g.NgDKcbtchapoCYJnYZ9JDIUggUM"

TOKEN19 = "Nzg4OTczOTE5NDIzNjkyODEx.X9rTjQ._T5kN71dkjiF2AmhX_yYr87IjCI"

TOKEN20 = "Nzg4OTc0Njg4OTM5OTMzNzE3.X9rUMA.vh8QSc5xzcc6TUt0JE9s_Sk5aTM"

TOKEN21 = "Nzg5MjAyNzc2MDQ2ODI5NTY5.X9upEQ.kOQFNCiky5IXLbsgoWiadgTxn_k"

TOKEN22 = "Nzg4NjQ3MTAwNDgwMzU2MzUy.X9mjDQ.ll9lBP1zFgWnmV-aSL_OXWfmYtU"

TOKEN23 = "Nzg4NjQ4Mjc5MjA2Mzk1OTY0.X9mkJA.i_bO-4h65auePb9Vu6CC-pGVqIU"

TOKEN24 = "Nzg4NjQ4ODQxMTc0OTc0NDk0.X9mkyA.cQnw2isCvw9eNabOmMAN8IrskwU"

TOKEN25 = "Nzg4NjY1NTg2MjEyNTM2MzUw.X9m0bQ.Xhdlz1hLDi2dv8J9mMJq1uQVEXY"

TOKEN26 = "Nzg4NjY2Mzc4NzIyNDc2MDYy.X9m0_w.kAaak-8_FtT7TtkPDZMfE225nJg"

TOKEN27 = "Nzg4NjY2OTI3MjIzNjY4NzM3.X9m1nA.Um-hnVagzud9cIoN8I2XmwFQBRI"

TOKEN28 = "Nzg4NjY4NjkzNjIxNTA2MDg4.X9m3Nw.j8Xb5nhcIk9kNh0KdRPxuMxzc2o"

TOKEN29 = "Nzg4NjY5NDM5NjUwMTY4ODQy.X9m31A.ZRRvSjMCqjq3BqayJCVwwDX9wzc"

TOKEN30 = "Nzg4NjgyMDY3NDk0OTYxMjIy.X9nD9w._awWq0NSxF9yNtxXntQWYxvcB9A"



#JOINER, LEAVER!!!

TARGET = "https://discordapp.com/api/v6/invites/7jUCTwhs"

LEAVE = 784390194585403354

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

client16 = discord.Client(self_bot = True)

client17 = discord.Client(self_bot = True)

client18 = discord.Client(self_bot = True)

client19 = discord.Client(self_bot = True)

client20 = discord.Client(self_bot = True)

client21 = discord.Client(self_bot = True)

client22 = discord.Client(self_bot = True)

client23 = discord.Client(self_bot = True)

client24 = discord.Client(self_bot = True)

client25 = discord.Client(self_bot = True)

client26 = discord.Client(self_bot = True)

client27 = discord.Client(self_bot = True)

client28 = discord.Client(self_bot = True)

client29 = discord.Client(self_bot = True)

client30 = discord.Client(self_bot = True)

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
   await client4.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN4})
   await SERVER.leave()
   print(f"Bot 4 is ready!!. Login as {client4.user.name}")

@client5.event
async def on_ready():
   SERVER = client5.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN5})
   await SERVER.leave()
   print(f"Bot 5 is ready!!. Login as {client5.user.name}")
   
@client6.event
async def on_ready():
   SERVER = client6.get_guild(LEAVE)
   await client6.change_presence(status=discord.Status.dnd)
   requests.post(TARGET,headers={'authorization':TOKEN6})
   await SERVER.leave()
   print(f"Bot 6 is ready!!. Login as {client6.user.name}")

@client7.event
async def on_ready():
   SERVER = client7.get_guild(LEAVE)
   await client7.change_presence(status=discord.Status.idle)
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
   await client9.change_presence(status=discord.Status.dnd)
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
   await client12.change_presence(status=discord.Status.idle)
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
   await client14.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN14})
   await SERVER.leave()
   print(f"Bot 14 is ready!!. Login as {client14.user.name}")

@client15.event
async def on_ready():
   SERVER = client15.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN15})
   await SERVER.leave()
   print(f"Bot 15 is ready!!. Login as {client15.user.name}")

@client16.event
async def on_ready():
   SERVER = client16.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN16})
   await SERVER.leave()
   print(f"Bot 16 is ready!!. Login as {client16.user.name}")

@client17.event
async def on_ready():
   SERVER = client17.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN17})
   await SERVER.leave()
   print(f"Bot 17 is ready!!. Login as {client17.user.name}")

@client18.event
async def on_ready():
   SERVER = client18.get_guild(LEAVE)
   await client18.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN18})
   await SERVER.leave()
   print(f"Bot 28 is ready!!. Login as {client18.user.name}")

@client19.event
async def on_ready():
   SERVER = client19.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN19})
   await SERVER.leave()
   print(f"Bot 19 is ready!!. Login as {client19.user.name}")

@client20.event
async def on_ready():
   SERVER = client20.get_guild(LEAVE)
   await client20.change_presence(status=discord.Status.dnd)
   requests.post(TARGET,headers={'authorization':TOKEN20})
   await SERVER.leave()
   print(f"Bot 20 is ready!!. Login as {client20.user.name}")

@client21.event
async def on_ready():
   SERVER = client21.get_guild(LEAVE)
   await client21.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN21})
   await SERVER.leave()
   print(f"Bot 21 is ready!!. Login as {client21.user.name}")

@client22.event
async def on_ready():
   SERVER = client22.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN22})
   await SERVER.leave()
   print(f"Bot 22 is ready!!. Login as {client22.user.name}")

@client23.event
async def on_ready():
   SERVER = client23.get_guild(LEAVE)
   await client23.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN23})
   await SERVER.leave()
   print(f"Bot 23 is ready!!. Login as {client23.user.name}")

@client24.event
async def on_ready():
   SERVER = client24.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN24})
   await SERVER.leave()
   print(f"Bot 24 is ready!!. Login as {client24.user.name}")

@client25.event
async def on_ready():
   SERVER = client25.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN25})
   await SERVER.leave()
   print(f"Bot 25 is ready!!. Login as {client25.user.name}")

@client26.event
async def on_ready():
   SERVER = client26.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN26})
   await SERVER.leave()
   print(f"Bot 26 is ready!!. Login as {client26.user.name}")

@client27.event
async def on_ready():
   SERVER = client27.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN27})
   await SERVER.leave()
   print(f"Bot 27 is ready!!. Login as {client27.user.name}")

@client28.event
async def on_ready():
   SERVER = client28.get_guild(LEAVE)
   await client28.change_presence(status=discord.Status.idle)
   requests.post(TARGET,headers={'authorization':TOKEN28})
   await SERVER.leave()
   print(f"Bot 28 is ready!!. Login as {client28.user.name}")

@client29.event
async def on_ready():
   SERVER = client29.get_guild(LEAVE)
   requests.post(TARGET,headers={'authorization':TOKEN29})
   await SERVER.leave()
   print(f"Bot 29 is ready!!. Login as {client29.user.name}")

@client30.event
async def on_ready():
   SERVER = client30.get_guild(LEAVE)
   await client30.change_presence(status=discord.Status.dnd)
   requests.post(TARGET,headers={'authorization':TOKEN30})
   await SERVER.leave()
   print(f"Bot 30 is ready!!. Login as {client30.user.name}")

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

loop.create_task(client16.start(TOKEN16, bot=False))
loop.create_task(client17.start(TOKEN17, bot=False))
loop.create_task(client18.start(TOKEN18, bot=False))
loop.create_task(client19.start(TOKEN19, bot=False))
loop.create_task(client20.start(TOKEN20, bot=False))

loop.create_task(client21.start(TOKEN21, bot=False))
loop.create_task(client22.start(TOKEN22, bot=False))
loop.create_task(client23.start(TOKEN23, bot=False))
loop.create_task(client24.start(TOKEN24, bot=False))
loop.create_task(client25.start(TOKEN25, bot=False))
loop.create_task(client26.start(TOKEN26, bot=False))
loop.create_task(client27.start(TOKEN27, bot=False))
loop.create_task(client28.start(TOKEN28, bot=False))
loop.create_task(client29.start(TOKEN29, bot=False))
loop.create_task(client30.start(TOKEN30, bot=False))

loop.run_forever()
