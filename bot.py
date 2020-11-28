import discord
import os
import datetime
import asyncio
import random
import requests
import youtube_dl


from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get

from discord.ext import commands

from youtube_dl import YoutubeDL
from requests import get


TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
client = commands.AutoShardedBot(command_prefix=":", intents=intents, help_command=none)


@client.event
async def on_ready():
	print("The bot is up!")
	print(client.user)

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Emilia Suffer"))

#--------------------------------Members logs----------------------------------
@client.event
async def on_message_edit(before, after):
    embed = discord.Embed(
        timestamp=after.created_at,
        description = "message was edited", color=0x982abc
        ) 
    embed.set_author(name=f'{before.author.name} {before.author.discriminator}', icon_url=before.author.avatar_url)
    embed.set_footer(text=f"Author ID:{before.author.id} • Message ID: {before.id}")
    embed.add_field(name=f'User: ', value=f'{before.author.mention}', inline=False)
    embed.add_field(name='Before:', value=before.content, inline=False)
    embed.add_field(name="After:", value=after.content, inline=False)
    channel = client.get_channel(780760893125689364)
    await channel.send(embed=embed)

@client.event
async def on_message_delete(message):
  
   embdel = discord.Embed(
        title='User Message deleted', color=0x982abc
     	)
   embdel.set_author(name='Subaru')
   embdel.add_field(name=f'User:', value=f'{message.author.mention}')
   embdel.add_field(name='message deleted', value=message.content)
   channel = client.get_channel(780760893125689364)
   await channel.send(embed=embdel)

@client.event
async def on_member_join(member):
    embmsg = discord.Embed(
        title='User joined:', color=0x982abc
        )
    embmsg.set_author(name="WonderBot")
    embmsg.add_field(name='User: ', value=f'{member.mention}(ID: {member.id})', inline=False)
    channel = client.get_channel(780760725299396629)
    await channel.send(embed=embmsg)

@client.event
async def on_member_remove(member):
    embmsg1 = discord.Embed(
        title='User left:', color=0x982abc
        )
    embmsg1.set_author(name="WonderBot")
    embmsg1.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id})', inline=False)
    channel = client.get_channel(780760725299396629)
    await channel.send(embed=embmsg1)
#--------------------------------Members logs----------------------------------

@client.command()
@commands.has_any_role("clear perms", "Admin")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
    kickembed = discord.Embed(
    title='User kicked:', color=0x982abc
    )
    kickembed.set_author(name="WonderBot", icon_url=" https://cdn.discordapp.com/avatars/772894741582708778/db69e1a3b55e924eaf79dd3bccedebd7.png?size=128 ")
    kickembed.add_field(name='User: ', value=f'{member.mention}(ID: {member.id}) ', inline=False)
    channel = client.get_channel(780760958242652160)
      
    await member.kick()

    await context.send('User ' + member.mention + ' has been kicked')
    await channel.send(embed=kickembed)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.Member):
    banembed = discord.Embed(
    title='User banned:', color=0x982abc
    )
    banembed.set_author(name="WonderBot", icon_url=" https://cdn.discordapp.com/avatars/772894741582708778/db69e1a3b55e924eaf79dd3bccedebd7.png?size=128 ")
    banembed.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id}) ', inline=False)
    channel = client.get_channel(780760958242652160)
    
    await member.ban()
    
    await context.send('User ' + member.mention + ' has been banned')
    await channel.send(embed=banembed)

@client.command()
async def help():
    embed=discord.Embed(title="Commands availble", description="commands:", color=0x7a219e)
embed.set_author(name="Subaru 1.0v")
embed.add_field(name="help", value="Shows commands availble", inline=False)
embed.add_field(name="play", value="plays a spesific music (under maintance)", inline=True)
embed.add_field(name="stop", value="stop the music (under maintenance)", inline=True)
embed.add_field(name="join", value="join a voice channel (under maintenance)", inline=True)
embed.add_field(name="leave", value="leaves a voice channel (under maintanance)", inline=True)
embed.add_field(name="ban", value="ban a member ?ban [user] [reason]", inline=True)
embed.add_field(name="kick", value="kick a member ?kick [user] [reason]", inline=True)
embed.add_field(name="clear", value="clear messages ?clear [value] default is 5 ", inline=True)
embed.set_footer(text="Bot Coding by ChibiSubaru#2483")
    await ctx.send(embed=embed)
#--------------------------------Music commands----------------------------------

#Get videos from links or from youtube search
def search(query):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
        try: requests.get(arg)
        except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else: info = ydl.extract_info(arg, download=False)
    return (info, info['formats'][0]['url'])


@client.command()
async def join(ctx, voice):
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command()
async def play(ctx, *, query):
    #Solves a problem I'll explain later
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    video, source = search(query)
    voice = get(client.voice_clients, guild=ctx.guild)

    await join(ctx, voice)
    await ctx.send(f'Now playing.')

    voice.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
    voice.is_playing()


if __name__ == "__main__":
    client.run(TOKEN)
