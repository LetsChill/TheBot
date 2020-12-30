import discord

from discord.ext import commands

from discord.utils import get

import discord.ext.commands

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
    async def kick(self, ctx, member: discord.Member=None, *, reason="No Reason Provided"):
      if not member:
        await ctx.send("you have to mention someone, or give there <ID> if they left!.\n\nkick <ID>/<mention> [Reason]")
        return
      
      if member == ctx.author:
        await ctx.send("You Can't Kick Your Self...")
        return

      if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
        await ctx.send("You Can't Kick A Moderator!")
        return

      try:
        await member.send(f"You Were Kicked From **{ctx.guild.name}** \n\nReason: **{reason}**")
        await member.kick(reason=f"Moderator: {ctx.author.name}\n\nReason: {reason}")
 
        guild = ctx.guild
        banembed = discord.Embed(
        title='User banned:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f'{member.name}\n\n (ID: {member.id}) ', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        channel.send(embed=banembed)
        ctx.send(f"{member.name} was kicked!")

      except:
        await member.kick(reason=f"Moderator: {ctx.author.name}\n\nReason: {reason}")
        guild = ctx.guild
        banembed = discord.Embed(
        title='User banned:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f'{member.name} (ID: {member.id}) ', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        channel.send(embed=banembed)
        ctx.send(f"{member.name} was kicked But Couldn't dm them")

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

#error_Handling-----

    @kick.error
    async def kick_error(self, ctx, error):
      await ctx.send("There was an error")
      if isinstance(error, commands.Forbidden):
          await ctx.send("I Dont Have Permissions To Kick.")
      else:
          raise error






def setup(client):
    client.add_cog(Moderator(client))

