import discord
import requests
import random

import os
import datetime
import asyncio
import random

from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()
client = commands.AutoShardedBot(command_prefix="-", intents=intents, help_command=None)


async def status():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Humans on {len(client.guilds)} Servers")
     asyncio.sleep(120)
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"-help for commands!")
     asyncio.sleep(120)





@client.event
async def on_ready():
     client.loop.create_task(status())
     print(f"Bot Is Ready!")
                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzcyODk0NzQxNTgyNzA4Nzc4.X6BUUg.5CXfanDNexURwqbjJwS-sdtWyNc")
