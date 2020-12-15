#might make a tut on how to add commands
import discord

import requests

from discord.ext import commands

token = "Nzc2MDQ5MzMxNjI3MDk4MTQz.X9g9kQ.gqOtml38QCN09pIw9Mjb5mJvb-Y"

token2 = "Nzc2MDQ1MzE0MzIyNTk1ODYw.X9hHGQ.e1Pd1nh5OHzdNNAVjUGEsIJ44fI"
client = commands.Bot("$$$", self_bot = True)

client2 = commands.Bot("$$$", self_bot = True)

@client.event
async def on_ready():
   print("Bot is ready!!")

@client2.event
async def on_ready():
   print("Bot is ready!!")

@client.command()
async def joinserver(mahlink):
    await client.accept_invite(mahlink)

client.run(token, bot=False)
client2.run(token2, bot=False)
