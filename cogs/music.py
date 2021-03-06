import discord
from discord.ext import commands
import DiscordUtils

music = DiscordUtils.Music()

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def join(self, ctx):
        if ctx.guild.voice_client is None:
             await ctx.author.voice.channel.connect() #Joins author’s voice channel
             await ctx.send("joined the channel!")
        else:
             await ctx.send("i am already in a voice channel ._.")


    @commands.command()
    async def leave(self, ctx):
        if ctx.guild.voice_client is not None:
             player = music.get_player(guild_id=ctx.guild.id)
             await player.stop()
             await ctx.voice_client.disconnect()
             await ctx.send("left the channel!")
        else:
             await ctx.send("i am not in a voice channel ._.")

    @commands.command()
    async def dc(self, ctx):
        if ctx.guild.voice_client is not None:
             player = music.get_player(guild_id=ctx.guild.id)
             await player.stop()
             await ctx.voice_client.disconnect()
             await ctx.send("left the channel!")
        else:
             await ctx.send("i am not in a voice channel ._.")


    @commands.command()
    async def play(self, ctx, *, url):
        if ctx.guild.voice_client is not None:
            player = music.get_player(guild_id=ctx.guild.id)
            if not player:
                player = music.create_player(ctx, ffmpeg_error_betterfix=True)
            if not ctx.voice_client.is_playing():
                await player.queue(url, search=True)
                song = await player.play()
                await ctx.send(f"Playing **{song.name}**")
            else:
                song = await player.queue(url, search=True)
                await ctx.send(f"Queued **{song.name}**")
        else:
            await ctx.author.voice.channel.connect()
            player = music.get_player(guild_id=ctx.guild.id)
            if not player:
                player = music.create_player(ctx, ffmpeg_error_betterfix=True)
            if not ctx.voice_client.is_playing():
                await player.queue(url, search=True)
                song = await player.play()
                await ctx.send(f"Playing **{song.name}**")
            else:
                song = await player.queue(url, search=True)
                await ctx.send(f"Queued **{song.name}**")


    @commands.command()
    async def pause(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f"Paused **{song.name}**")

    @commands.command()
    async def resume(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f"Resumed **{song.name}**")

    @commands.command()
    async def stop(self, ctx):
       player = music.get_player(guild_id=ctx.guild.id)
       song = await player.pause()
       await ctx.send(f"Paused **{song.name}**")

    @commands.command()
    async def loop(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            await ctx.send(f"Enabled loop for **{song.name}**")
        else:
            await ctx.send(f"Disabled loop for **{song.name}**")

    @commands.command()
    async def queue(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")

    @commands.command()
    async def np(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = player.now_playing()
        await ctx.send(song.name)
        
    @commands.command()
    async def skip(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        data = await player.skip(force=True)
        if len(data) == 2:
            await ctx.send(f"Skipped from **{data[0].name}** to **{data[1].name}**")
        else: 
            await ctx.send(f"Skipped **{data[0].name}**")

    @commands.command()
    async def remove(self, ctx, index):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        await ctx.send(f"Removed **{song.name}** from queue")
    
    
def setup(client):
    client.add_cog(Music(client))
