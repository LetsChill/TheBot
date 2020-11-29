
import discord
import os
import datetime
import asyncio
import random

from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
client = commands.AutoShardedBot(command_prefix="?", intents=intents, help_command=None)

@client.event
async def on_ready():
	print("The bot is up!")
	print(client.user)

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Emilia Suffer"))
     
@client.event()
async def on_member_join(member):
    guild = member.guild
    channel = get(guild.channels, name = "test")
    await channel.edit(name = f"Member Count : {guild.members}")
    
@client.event()
async def on_member_remove(member):
    guild = member.guild
    channel = get(guild.channels, name = "test")
    await channel.edit(name = f"Member Count : {guild.members}")
                        

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == "__main__":
    client.run(TOKEN)
