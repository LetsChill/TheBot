import discord
import os
import datetime
import asyncio
import random
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
client = commands.Bot(command_prefix = ':', intents=intents)

@client.event
async def on_ready():
	print("The bot is up!")
	print(client.user)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Servers :help'))
 

@client.event
async def on_message_edit(before, after):
    embed = discord.Embed(
        timestamp=after.created_at,
        description = "message was edited",
        colour = discord.Colour(0x982abc)
        ) 
    embed.set_author(name=f'{before.author.name} {before.author.discriminator}', icon_url=before.author.avatar_url)
    embed.set_footer(text=f"Author ID:{before.author.id} • Message ID: {before.id}")
    embed.add_field(name=f'User: ', value=f'{before.author.mention}', inline=False)
    embed.add_field(name='Before:', value=before.content, inline=False)
    embed.add_field(name="After:", value=after.content, inline=False)
    channel = client.get_channel(780760893125689364)
    await channel.send(embed=embed)

@client.event
Async def on_member_join(member)
    embed=discord.Embed(title=User joined:, color=0x982abc)
        embed.set_author(name=WonderBot,icon_url=https://cdn.discordapp.com/avatars/772894741582708778/db69e1a3b55e924eaf79dd3bccedebd7.png?size=128)
        embed.add_field(name=User:, value=f"{member.mention} (ID: {member.id}', inline=False)
        channel = client.get_channel(780760725299396629)
await channel.send(embed=embed)

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

