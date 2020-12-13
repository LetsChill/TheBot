#might make a tut on how to add commands
import discord
from discord.ext import commands

token = "NTEzMzUxOTE3NDgxNjIzNTcy.X9Yziw.bp_cWSzIE1YaLKNlmR3H8-pQBEM"

client = commands.Bot("$$$", self_bot = True)

@client.event
async def on_ready():
        @bot.event
async def on_ready():
        activity = discord.Game(name="Cyperpunk 2077", type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
	print("Bot is ready!!")

client.run(token, bot=False)
