
import discord
import os
import datetime
import asyncio
import random

from discord.ext import commands
from discord.utils import get

EMAIL = os.getenv("EMAIL")

PASS = os.getenv("PASS")



intents = discord.Intents().all()
client = commands.AutoShardedBot(command_prefix="?", intents=intents, help_command=None)

@client.event
async def on_ready():
	print("The bot is up!")
	print(client.user)

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="?help for guild"))
     
@client.event
async def on_message(message):
    if(message.channel.id == "776751694570061884"):
        await client.add_reaction(message, "✅")
                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == "__main__":
    client.run(EMAIL, PASS)
