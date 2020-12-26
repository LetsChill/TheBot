import discord

from discord.ext import commands

from discord.utils import get

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
         await ctx.channel.purge(limit=1)
         await ctx.channel.purge(limit=amount)
         await ctx.channel.send(f"purged {amount} messages", delete_after=4)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member):
       if member.guild_permissions.kick_members or member.guild_permissions.ban_members:
            await context.send("You cant kick A mod/admin")
       else:
            guild = context.guild
            kickembed = discord.Embed(
            title='User kicked:', color=0x982abc
            )
            kickembed.set_author(name="Subary")
            kickembed.add_field(name='User: ', value=f'{member.mention}(ID: {member.id}) ', inline=False)
            channel = discord.utils.get(guild.channels, name='mod-logs')
            await member.kick()
                
        
            await context.send('User ' + member.mention + ' has been kicked')
            await channel.send(embed=kickembed)



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member):
       if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
            await context.send("you cant ban a mod/admin")
       else:
            guild = context.guild
            banembed = discord.Embed(
            title='User banned:', color=0x982abc
            )
            banembed.set_author(name="Subary")
            banembed.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id}) ', inline=False)
            channel = discord.utils.get(guild.channels, name='mod-logs')
            await member.ban()
    
            await context.send('User ' + member.mention + ' has been banned')
            await channel.send(embed=banembed)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def softban(self, context, member: discord.Member):
       if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
            await context.send("you cant soft ban a mod/admin")
       else:
            guild = context.guild
            banembed = discord.Embed(
            title='User soft banned:', color=0x982abc
            )
            banembed.set_author(name="Subary")
            banembed.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id}) ', inline=False)
            channel = discord.utils.get(guild.channels, name='mod-logs')
            await member.ban()
            await member.unban()
    
            await context.send('User ' + member.mention + ' has been soft banned')
            await channel.send(embed=banembed)



    @commands.command()
    async def setdelay(self, ctx, seconds: int):
       if ctx.author.guild_permissions.manage_channels:
              guild = ctx.guild
              Delemb = discord.Embed(
              title='Channel delay set:', color=0x982abc
              )
              Delemb.add_field(name=f'Moderator: {ctx.author.mention} ', value=f"Delay set To {seconds} seconds", inline=False)
              channel = discord.utils.get(guild.channels, name='mod-logs')
              await ctx.channel.edit(slowmode_delay=seconds)
              await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")
              await channel.send(embed=Delemb)
       else:
              await ctx.send("You dont Have Permission for that!")


def setup(client):
    client.add_cog(Moderator(client))

