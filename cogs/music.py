import discord
import youtube_dl

from discord.ext import commands

from youtube_dl import YoutubeDL
from requests import get

from discord import FFmpegPCMAudio

from discord.utils import get

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client


#Get videos from links or from youtube search
    def search(query):
        with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
            try: requests.get(arg)
            except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else: info = ydl.extract_info(arg, download=False)
        return (info, info['formats'][0]['url'])

    @commands.command()
    async def join(self, ctx, voice):
        channel = self.ctx.author.voice.channel

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
    #Solves a problem I'll explain later
        FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        video, source = search(query)
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        await join(ctx, voice)
        await ctx.send(f'Now playing {info['title']}.')


def setup(client):
    client.add_cog(Music(client))
