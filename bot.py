#might make a tut on how to add commands
import discord

from discord.ext import commands

token = "Nzc2MDQ5MzMxNjI3MDk4MTQz.X9g9kQ.gqOtml38QCN09pIw9Mjb5mJvb-Y"

client = commands.Bot("$$$", self_bot = True)

@client.event
async def on_ready():
   print("Bot is ready!!")

@client.event
async def on_ready():
    await client.accept_invite("https://discord.gg/zQ8PCcvX")
    print("Server joined!")
client.run(token, bot=False)
