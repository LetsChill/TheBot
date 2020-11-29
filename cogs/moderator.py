import discord

from discord.ext import commands

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client


@commands.command()
@commands.has_any_role("clear perms", "Admin")
async def clear(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(self, context, member: discord.Member):
    kickembed = discord.Embed(
    title='User kicked:', color=0x982abc
    )
    kickembed.set_author(name="WonderBot", icon_url=" https://cdn.discordapp.com/avatars/772894741582708778/db69e1a3b55e924eaf79dd3bccedebd7.png?size=128 ")
    kickembed.add_field(name='User: ', value=f'{member.mention}(ID: {member.id}) ', inline=False)
    channel = self.client.get_channel(780760958242652160)
      
    await member.kick()

    await context.send('User ' + member.mention + ' has been kicked')
    await channel.send(embed=kickembed)


@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(self, context, member: discord.Member):
    banembed = discord.Embed(
    title='User banned:', color=0x982abc
    )
    banembed.set_author(name="WonderBot", icon_url=" https://cdn.discordapp.com/avatars/772894741582708778/db69e1a3b55e924eaf79dd3bccedebd7.png?size=128 ")
    banembed.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id}) ', inline=False)
    channel = self.client.get_channel(780760958242652160)
    
    await member.ban()
    
    await context.send('User ' + member.mention + ' has been banned')
    await channel.send(embed=banembed)

@commands.command()
async def help(context):
    embhelp=discord.Embed(
    title="Commands availble", description="commands:", color=0x7a219e 
    )
    embhelp.set_author(name="Subaru 1.0v")
    embhelp.add_field(name="help", value="Shows commands availble", inline=False)
    embhelp.add_field(name="play", value="plays a spesific music (under maintance)", inline=True)
    embhelp.add_field(name="stop", value="stop the music (under maintenance)", inline=True)
    embhelp.add_field(name="join", value="join a voice channel (under maintenance)", inline=True)
    embhelp.add_field(name="leave", value="leaves a voice channel (under maintanance)", inline=True)
    embhelp.add_field(name="ban", value="ban a member ?ban [user] [reason]", inline=True)
    embhelp.add_field(name="kick", value="kick a member ?kick [user] [reason]", inline=True)
    embhelp.add_field(name="clear", value="clear messages ?clear [value] default is 5 ", inline=True)
    embhelp.set_footer(text="Bot Coding by ChibiSubaru#2483")
    await context.send(embed=embhelp)




def setup(client):
    client.add_cog(Logging(client))



