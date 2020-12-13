#might make a tut on how to add commands
import discord
from discord.ext import commands
from lol import token

client = commands.Bot("$$$", self_bot = True)

@client.event
async def on_ready():
	print("Bot is ready!!")

client.run(token, bot=False)
