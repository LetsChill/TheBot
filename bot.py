
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
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Under Development in this moment")
     
@client.command(ctx)
async def donate():
    dembed=discord.Embed(
    title="Donate me!", description="http://paypal.me/LetsChiLI", color=0x7a219e 
    )
    await ctx.send(embed=dembed)
                        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == "__main__":
    client.run(TOKEN)
