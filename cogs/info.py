import discord

from discord.ext import commands

from discord.utils import get

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
   
        embed = discord.Embed(
        title=name + " Server Information",
        color=discord.Color.blue()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    async def help(self, context):
        embhelp=discord.Embed(
        title="Commands availble", description="commands:", color=0x7a219e 
        )
        embhelp.set_author(name="Costum Bot 1.1v, *prefix is* **:**")
        embhelp.add_field(name="help", value="Shows commands availble", inline=False)
        embhelp.add_field(name="play", value="play [url] or ?play [search engine]", inline=True)
        embhelp.add_field(name="stop", value="stop the music and makes the bot leaves the channel", inline=True)
        embhelp.add_field(name="join", value="join a voice channel with [ID] of the channel", inline=True)
        embhelp.add_field(name="leave", value="makes the bot leaves the channel", inline=True)
        embhelp.add_field(name="queue", value="shows tye queue of songs will be played in future", inline=True)
        embhelp.add_field(name="remove", value="remove [order number in the queue], to remove any playlist from the queue", inline=True)
        embhelp.add_field(name="donate", value="Make my Day amazing and buy me a cake!", inline=True)
        embhelp.set_footer(text="Bot Coding by HАJякя#2483")
        await context.send(embed=embhelp)

    @commands.command()
    async def donate(self, context):
        embdon=discord.Embed(
        title="Ways to donate!", description=":)", color=0x7a219e 
        )
        embdon.set_author(name="Donate To LetsChill")
        embdon.add_field(name="Patreon!", value="http://patreon.com/LetsChill", inline=False)
        embdon.add_field(name="Cripto/bitcoins", value="https://donate.subaru.cf/", inline=True)
        await context.send(embed=embdon)

def setup(client):
    client.add_cog(Info(client))
