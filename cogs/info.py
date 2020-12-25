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
    async def help(self, ctx, arg1: str = None):
         if arg1 == "music":
              embhelp=discord.Embed(
              title="Commands availble", description="commands:", color=0x7a219e 
              )
              embhelp.set_author(name="Subary Bot 2.0v, prefix is :")
              embhelp.add_field(name="play", value="play [url] or play [search engine]", inline=True)
              embhelp.add_field(name="stop", value="stop the music and makes the bot leaves the channel", inline=True)
              embhelp.add_field(name="join", value="join a voice channel with [ID] of the channel", inline=True)
              embhelp.add_field(name="leave", value="makes the bot leaves the channel", inline=True)
              embhelp.add_field(name="queue", value="shows the queue of songs will be played in future", inline=True)
              embhelp.add_field(name="remove", value="remove [order number in the queue], to remove any playlist from the queue", inline=True)
              await ctx.send(embed=embhelp)

         elif arg1 == "mod":
              embhelp2=discord.Embed(
              title="Commands availble", description="commands:", color=0x7a219e 
              )
              embhelp2.set_author(name="Costum Bot 1.1v, prefix is :")
              embhelp2.add_field(name="setup", value="How to setup logging!", inline=False)
              embhelp2.add_field(name="kick", value="kick [mention] only to people who have kick perms, be sure to put the bot role above members.", inline=True)
              embhelp2.add_field(name="ban", value="ban [mention] only to people who have ban perms, be sure to put the bot role above members.", inline=True)
              embhelp2.add_field(name="clear", value="clear [number], bulk delete messages, set to 1 by default", inline=True)
              await ctx.send(embed=embhelp2)

         elif arg1 == None:
              embhelp3=discord.Embed(
              title="Commands availble", description="commands:", color=0x7a219e 
              )
              embhelp3.set_author(name="Subary Bot 2.0v, prefix is :")
              embhelp3.add_field(name="help Music", value="Music commands help!", inline=False)
              embhelp3.add_field(name="help mod", value="Moderation commands help!", inline=False)
              embhelp3.add_field(name="donate", value="How can you donate!", inline=False)
              embhelp3.add_field(name="invite", value="Invite me!, or other stuff", inline=False)
              embhelp3.set_footer(text="Bot Coding by LetsChill#0001")
              await ctx.send(embed=embhelp3)

         else:
              embhelp4=discord.Embed(
              title="invalid Argument", description="Invalid Argument was passed", color=0x7a219e
              )
              await ctx.send(embed=embhelp4)

    @commands.command()
    async def donate(self, context):
        embdon=discord.Embed(
        title="Ways to donate!", description=":)", color=0x7a219e 
        )
        embdon.set_author(name="Donate To LetsChill")
        embdon.add_field(name="Patreon!", value="http://patreon.com/LetsChill", inline=False)
        embdon.add_field(name="Cripto/bitcoins", value="https://donate.subaru.cf/", inline=True)
        await context.send(embed=embdon)

    @commands.command()
    async def invite(self, context):
        embdon=discord.Embed(
        title="Invite me? Or join our support server!", description=":)", color=0x7a219e 
        )
        embdon.set_author(name="Invites")
        embdon.add_field(name="Invite me!", value="https://discord.subaru.cf/", inline=False)
        embdon.add_field(name="Official Site!", value="https://subaru.cf/", inline=False)
        embdon.add_field(name="Support Server!", value="https://invite.subaru.cf/", inline=True)
        await context.send(embed=embdon)

def setup(client):
    client.add_cog(Info(client))
