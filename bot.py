import discord
import os
import datetime
import asyncio
import random

from discord.ext import commands
from discord.utils import get

TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
client = commands.AutoShardedBot(command_prefix="?", intents=intents, help_command=None)

@client.event
async def on_ready():
	print("The bot is up!")
	print(client.user)
	
@client.event
async def on_message(message):
	channel = client.get_channel(784103436861440010)
	await channel.send("<@711885122126741524>")
	
@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="?help for guild"))
                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')
       


if __name__ == "__main__":
    client.run(TOKEN)