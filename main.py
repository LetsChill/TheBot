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
client = commands.AutoShardedBot(command_prefix=":", intents=intents, help_command=None)
	
client.change_stats.start()

client.change_stats2.start()

@tasks.loop(seconds=30.0)
async def change_stats():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Humans on {len(client.guilds)} Servers , :help"))
     print(f"Bot Is Up {client.user.name}")

@tasks.loop(seconds=60.0)
async def change_stats2():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"invite.subary.cf ! Visit us!"))
     print(f"Is looping! {client.user.name}")

                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzcyODk0NzQxNTgyNzA4Nzc4.X6BUUg.bPUU5aXbibEDEZl8JQ1cs_DqmsY")
