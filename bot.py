import discord
import os
import datetime
import asyncio
import random
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
client = commands.Bot(command_prefix = ':')

@client.event
async def on_ready():
	print("The bot is up!")
	print(client.user)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Servers :help'))
 
@client.command()
@commands.has_any_role("clear perms", "Admin")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
     
    await member.kick()
    await context.send('User ' + member.mention + ' has been kicked')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.Member):
     
    await member.ban()
    await context.send('User ' + member.mention + ' has been banned')

if __name__ == "__main__":
    client.run(TOKEN)

