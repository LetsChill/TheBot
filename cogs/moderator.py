import discord

from discord.ext import commands

from discord.utils import get

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.command()

    @commands.command()
    @commands.has_any_role("clear perms", "Admin")
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f"purged {amount} messages", delete_after=4)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member):
        guild = context.guild
        kickembed = discord.Embed(
        title='User kicked:', color=0x982abc
        )
        kickembed.set_author(name="WonderBot", icon_url=" https://cdn.discordapp.com/avatars/772894741582708778/db69e1a3b55e924eaf79dd3bccedebd7.png?size=128 ")
        kickembed.add_field(name='User: ', value=f'{member.mention}(ID: {member.id}) ', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await member.kick()
                
        
        await context.send('User ' + member.mention + ' has been kicked')
        await channel.send(embed=kickembed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member):
        guild = context.guild
        banembed = discord.Embed(
        title='User banned:', color=0x982abc
        )
        banembed.set_author(name="WonderBot", icon_url=" https://cdn.discordapp.com/avatars/772894741582708778/db69e1a3b55e924eaf79dd3bccedebd7.png?size=128 ")
        banembed.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id}) ', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await member.ban()
    
        await context.send('User ' + member.mention + ' has been banned')
        await channel.send(embed=banembed)

    @commands.command()
    async def help(self, context):
        embhelp=discord.Embed(
        title="Commands availble", description="commands:", color=0x7a219e 
        )
        embhelp.set_author(name="Costum Bot 1.1v")
        embhelp.add_field(name="help", value="Shows commands availble", inline=False)
        embhelp.add_field(name="play", value="?play [url] or ?play [search engine]", inline=True)
        embhelp.add_field(name="stop", value="stop the music and makes the bot leaves the channel", inline=True)
        embhelp.add_field(name="join", value="join a voice channel with [ID] of the channel", inline=True)
        embhelp.add_field(name="leave", value="makes the bot leaves the channel", inline=True)
        embhelp.add_field(name="queue", value="shows tye queue of songs will be played in future", inline=True)
        embhelp.add_field(name="remove", value="?remove [order number in the queue], to remove any playlist from the queue", inline=True)
        embhelp.add_field(name="setup", value="server owner and admin only!, set up the logging system!", inline=True)
        embhelp.add_field(name="Lost?", value="Join our server! https://invite.subaru.cf/", inline=True)
        embhelp.set_footer(text="Bot Coding by LetsChill#0001")
        await context.send(embed=embhelp)
        
        

    @commands.command()
    async def copy(self, ctx):
      with open("messages.txt", "w") as f:
          async for message in ctx.history(limit=1000):
              f.write(message.content + "\n")

      await ctx.send("Done! copied 1k messages!")
      
        




def setup(client):
    client.add_cog(Moderator(client))

