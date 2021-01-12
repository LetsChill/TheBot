#might make a tut on how to add commands
import discord
from discord.ext import commands

token = "mfa.-G0rObP9WoC20lg2b2qPh9y-THR3oooEpmzwCgHprDKaH_inpm2TEYOi7auHUmiWzmKpwRPB1omrx6pZ_5d7"
client = commands.Bot("$$$", self_bot = True)

@client.event
async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name="Face Reveal!!", url="https://youtu.be/HP362ccZBmY"))
	print("Bot is ready!!")

client.run(token, bot=False)
