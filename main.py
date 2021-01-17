#might make a tut on how to add commands
import discord
from discord.ext import commands

TOKEN = "mfa.-G0rObP9WoC20lg2b2qPh9y-THR3oooEpmzwCgHprDKaH_inpm2TEYOi7auHUmiWzmKpwRPB1omrx6pZ_5d7"

client = discord.Client(self_bot = True)

@client.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Kimi No Na Wa | Your name | Half way there"))

client.run(TOKEN, bot=False)
