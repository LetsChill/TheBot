#might make a tut on how to add commands
import discord
from discord.ext import commands

TOKEN = "mfa.-G0rObP9WoC20lg2b2qPh9y-THR3oooEpmzwCgHprDKaH_inpm2TEYOi7auHUmiWzmKpwRPB1omrx6pZ_5d7"
client = commands.Bot("$$$", self_bot = True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Just Chilling", url="https://youtu.be/HP362ccZBmY")

client.run(TOKEN, bot=False)
