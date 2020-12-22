import discord
import requests
import random

import os
import datetime
import asyncio
import random

import flask
import keep_alive

from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()
client = commands.AutoShardedBot(command_prefix="?", intents=intents, help_command=None)
	
@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="?help For Information!!!"))
     print(f"Bot Is Up {client.user.name}")
                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')
       
keep_alive.keep_alive()
client.run("NzcyODk0NzQxNTgyNzA4Nzc4.X6BUUg.bPUU5aXbibEDEZl8JQ1cs_DqmsY")