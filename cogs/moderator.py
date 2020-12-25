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
       if member.guild_permissions.kick_members:
            await context.send("You cant kick A mod/admin")
       else:
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
       if member.guild_permissions.ban_members:
            await context.send("you cant ban a mod/admin")
       else:
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

def setup(client):
    client.add_cog(Moderator(client))

