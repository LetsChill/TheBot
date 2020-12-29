import discord

from discord.ext import commands

from discord.utils import get

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=1):
         if ctx.author.guild_permissions.manage_messages:
          
              await ctx.channel.purge(limit=1)
              await ctx.channel.purge(limit=amount)
              await ctx.channel.send(f"purged {amount} messages", delete_after=4)
         else:
              await ctx.channel.send("you dont have permissions to do so!", delete_after=4)

    @commands.command()
    async def kick(self, ctx, member: discord.Member):
        if client.user.guild_permussions.kick_members:
            if ctx.author.guild_permissions.kick_members or ctx.guild_permissions.ban_members:
  
                 if member.guild_permissions.kick_members or member.guild_permissions.ban_members:
                      await ctx.send("You Cant Kick A Mod/Admin!")

                 else:
                      guild = ctx.guild
                      kickembed = discord.Embed(
                      title='User kicked:', color=0x982abc
                      )
                      kickembed.set_author(name="Subary")
                      kickembed.add_field(name='User: ', value=f'{member.mention}(ID: {member.id}) ', inline=False)
                      channel = discord.utils.get(guild.channels, name='mod-logs')
                      await member.kick()
        
                      await ctx.send('User ' + member.mention + ' has been kicked')
                      await channel.send(embed=kickembed)

            else:
                 await ctx.send("you Dont Have Permissions To Kick!")
        else:
             await ctx.send("i dont have permissions!")


    @commands.command()
    async def ban(self, ctx, member: discord.Member):
       if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.ban_members:

            if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
                 await ctx.send("You Cant Ban A Mod/Admin!")

           

            else:
                 guild = ctx.guild
                 banembed = discord.Embed(
                 title='User banned:', color=0x982abc
                 )
                 banembed.set_author(name="Subary")
                 banembed.add_field(name=f'User: ', value=f'{member.name} (ID: {member.id}) ', inline=False)
                 channel = discord.utils.get(guild.channels, name='mod-logs')
                 await member.ban()
    
                 await ctx.send('User ' + member.mention + ' has been banned')
                 await channel.send(embed=banembed)

       else:
            await context.send("You Dont Have Permissions To Ban!")


    @commands.command()
    async def softban(self, ctx, member: discord.Member):
       if ctx.author.guild_permissions.kick_members or member.guild_permissions.ban_members:

            if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
                 await ctx.send("you cant soft ban a mod/admin")

     

            else:
                 guild = ctx.guild
                 banembed = discord.Embed(
                 title='User soft banned:', color=0x982abc
                 )
                 banembed.set_author(name="Subary")
                 banembed.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id}) ', inline=False)
                 channel = discord.utils.get(guild.channels, name='mod-logs')
                 await member.ban()
                 await member.unban()
    
                 await ctx.send('User ' + member.mention + ' has been soft banned')
                 await channel.send(embed=banembed)

       else:
            await ctx.send("You Cant SoftBan A Mod/Admin!")



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

