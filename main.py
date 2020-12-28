import discord
import requests
import random

import os
import datetime
import asyncio
import random

from discord.ext import commands

from discord_slash import SlashCommand
from discord_slash import SlashContext

from discord.utils import get


intents = discord.Intents().all()
client = commands.AutoShardedBot(command_prefix="&", intents=intents, help_command=None)
slash = SlashCommand(bot)

async def status_change():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Humans on {len(client.guilds)} Servers , &help"))
     await asyncio.sleep(100)
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"&help, helping humans getting perfect!"))
     await asyncio.sleep(100)

@slash.slash(name="test")
async def Test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])



@client.event
async def on_ready():
     client.loop.create_task(status_change())
     print(f"Bot Is Ready!")
                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

client.run("NzcyODk0NzQxNTgyNzA4Nzc4.X6BUUg.5CXfanDNexURwqbjJwS-sdtWyNc")
