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
    async def kick(self, ctx, member: discord.Member=None, *, arg=None):
      if not member:
        await ctx.send("you have to mention someone,\nkick <mention> [Reason]")
        return
      
      if member == ctx.author:
        await ctx.send("You Can't Kick Your Self...")
        return

      if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
        await ctx.send("You Can't Kick A Moderator!")
        return

      try:
        await member.send(f"You Were Kicked From **{ctx.guild.name}** \n\nReason: **{arg}**")
        await member.kick(reason=f"Moderator: {ctx.author.name}\n\nReason: {arg}")
 
        guild = ctx.guild
        banembed = discord.Embed(
        title='User banned:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f'{member.name}\n(ID: {member.id})\nModerator: {ctx.author.mention}\nReason:\n{arg} ', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await channel.send(embed=banembed)
        await ctx.send(f"{member.name} was kicked!")

      except discord.Forbidden:
        await ctx.send(f"I don't have permissions to kick")



      except:
        await member.kick(reason=f"Moderator: {ctx.author.name}\n\nReason: {arg}")
        guild = ctx.guild
        banembed = discord.Embed(
        title='User kicked:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f"{member.name}\n(ID: {member.id})\nModerator: {ctx.author.mention}\nReason:\n{arg} ", inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await channel.send(embed=banembed)
        await ctx.send(f"{member.name} was kicked But Couldn't dm them")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, arg):

      if not member:
        await ctx.send("you have to mention someone.\n\nban <mention> [Reason]")
        return
   
   
      if member == ctx.author:
        await ctx.send("You Can't ban Your Self...")
        return


      if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
        await ctx.send("You Can't ban A Moderator!")
        return


      try:
        await member.send(f"You Were Banned From **{ctx.guild.name}** \n\nReason: **{arg}**")
        await member.ban(reason=f"Moderator: {ctx.author.name}\n\nReason: {arg}")
 
        guild = ctx.guild
        banembed = discord.Embed(
        title='User banned:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f'{member.name}\n(ID: {member.id})\nModerator: {ctx.author.mention}\nReason:\n{arg}', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await channel.send(embed=banembed)
        await ctx.send(f"{member.name} was kicked!")


      except:
        await member.kick(reason=f"Moderator: {ctx.author.name}\n\nReason: {arg}")
        guild = ctx.guild
        banembed = discord.Embed(
        title='User banned:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f'{member.name}\n\n (ID: {member.id}) ', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await channel.send(embed=banembed)
        await ctx.send(f"{member.name} was kicked But Couldn't dm them")


    @commands.command()
    async def softban(self, ctx, member: discord.Member):
      if not member:
        await ctx.send("you have to mention someone.\n\nsoftban <mention> [Reason]")
        return
      
      if member == ctx.author:
        await ctx.send("You Can't softban Your Self...")
        return

      if member.guild_permissions.ban_members or member.guild_permissions.kick_members:
        await ctx.send("You Can't SoftBan A Moderator!")
        return

      try:
        await member.send(f"You Were softbanned From **{ctx.guild.name}** \n\nReason: **{arg}**")
        await member.ban(reason=f"Moderator: {ctx.author.name}\n\nReason: {arg}")
        await member.unban(reason="Soft ban Unbanning")
 
        guild = ctx.guild
        banembed = discord.Embed(
        title='User Softbanned:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f'{member.name}\n(ID: {member.id})\nModerator: {ctx.author.mention}\nReason:\n{arg} ', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await channel.send(embed=banembed)
        await ctx.send(f"{member.name} was kicked!")

      except discord.Forbidden:
        await ctx.send(f"I don't have permissions to ban")



      except:
        await member.ban(reason=f"Moderator: {ctx.author.name}\n\nReason: {arg}")
        await member.unban(reason="Soft ban Unbanning")
        guild = ctx.guild
        banembed = discord.Embed(
        title='User softbanned:', color=0x982abc
        )
        banembed.set_author(name="Subary")
        banembed.add_field(name=f'User: ', value=f'{member.display.name}', inline=False)
        channel = discord.utils.get(guild.channels, name='mod-logs')
        await channel.send(embed=banembed)
        await ctx.send(f"{member.name} was softbanned But Couldn't dm them")


    @commands.command()
    async def setdelay(self, ctx, seconds: int):
       if not seconds:
         await ctx.send("you need to spesify a number to set slowmode!")
       
       try:
           if ctx.author.guild_permissions.kick_members:
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

       except discord.Forbidden:
         ctx.send("i dont Have manage_channels permissions!")

def setup(client):
    client.add_cog(Moderator(client))

