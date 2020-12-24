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

@client.event
async def on_member_join(member):
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Humans on {len(client.guilds)} Servers , :help"))
     print(f"Tada! {member.user.name}")
                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzcyODk0NzQxNTgyNzA4Nzc4.X6BUUg.bPUU5aXbibEDEZl8JQ1cs_DqmsY")
