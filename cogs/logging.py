import discord

from discord.ext import commands

from discord.utils import get

class Logging(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        embed = discord.Embed(
        timestamp=after.created_at,
        description = "message was edited", color=0x982abc
        ) 
        embed.set_author(name=f'{before.author.name} {before.author.discriminator}', icon_url=before.author.avatar_url)
        embed.set_footer(text=f"Author ID:{before.author.id} • Message ID: {before.id}")
        embed.add_field(name=f'User: ', value=f'{before.author.mention}', inline=False)
        embed.add_field(name='Before:', value=before.content, inline=False)
        embed.add_field(name="After:", value=after.content, inline=False)
        channel = self.client.get_channel(784105832509341706)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
  
        embdel = discord.Embed(
        title='User Message deleted', color=0x982abc
        )
        embdel.set_author(name='Subaru')
        embdel.add_field(name=f'User:', value=f'{message.author.mention}')
        embdel.add_field(name='message deleted', value=message.content)
        channel = self.client.get_channel(784105832509341706)
        await channel.send(embed=embdel)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        channel = get(guild.channels, name = "Member Counter:")
        await channel.edit(name = f"Member Counter: {guild.member_count}")
        

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        channel = get(guild.channels, name = "Member Counter:")
        await channel.edit(name = f"Member Counter: {guild.member_count}")

def setup(client):
    client.add_cog(Logging(client))
