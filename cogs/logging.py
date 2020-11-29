import discord

from discord.ext import commands

class Logging(commands.Cog):

    def __init__(self, client)
        self.client = client

    @commands.cog.listener()
    async def on_message_edit(before, after):
    embed = discord.Embed(
        timestamp=after.created_at,
        description = "message was edited", color=0x982abc
        ) 
    embed.set_author(name=f'{before.author.name} {before.author.discriminator}', icon_url=before.author.avatar_url)
    embed.set_footer(text=f"Author ID:{before.author.id} • Message ID: {before.id}")
    embed.add_field(name=f'User: ', value=f'{before.author.mention}', inline=False)
    embed.add_field(name='Before:', value=before.content, inline=False)
    embed.add_field(name="After:", value=after.content, inline=False)
    channel = client.get_channel(780760893125689364)
    await channel.send(embed=embed)

    @commands.cog.listener()
    async def on_message_delete(message):
  
    embdel = discord.Embed(
         title='User Message deleted', color=0x982abc
         )
    embdel.set_author(name='Subaru')
    embdel.add_field(name=f'User:', value=f'{message.author.mention}')
    embdel.add_field(name='message deleted', value=message.content)
    channel = client.get_channel(780760893125689364)
    await channel.send(embed=embdel)

    @commands.cog.listener()
    async def on_member_join(member):
    embmsg = discord.Embed(
        title='User joined:', color=0x982abc
        )
    embmsg.set_author(name="WonderBot")
    embmsg.add_field(name='User: ', value=f'{member.mention}(ID: {member.id})', inline=False)
    channel = client.get_channel(780760725299396629)
    await channel.send(embed=embmsg)

    @commands.cog.listener()
    async def on_member_remove(member):
    embmsg1 = discord.Embed(
        title='User left:', color=0x982abc
        )
    embmsg1.set_author(name="WonderBot")
    embmsg1.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id})', inline=False)
    channel = client.get_channel(780760725299396629)
    await channel.send(embed=embmsg1) 


def setup(client):
    client.add_cog(Logging(client))