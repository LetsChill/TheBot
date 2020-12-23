import discord

from discord.ext import commands

from discord.utils import get

class Logging(commands.Cog):




    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def setup(self, ctx):
        await ctx.send("To setup the logging system, create 3 channels with the names: **member-logs**, **message-logs** and **mod-logs**")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong!🏓 Bot Latency was {round(self.client.latency * 1000)}ms")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        guild = before.guild
        embed = discord.Embed(
           
        timestamp=after.created_at,
        description = "message was edited", color=0x982abc
        ) 
        embed.set_author(name=f'{before.author.name} {before.author.discriminator}', icon_url=before.author.avatar_url)
        embed.set_footer(text=f"Author ID:{before.author.id} • Message ID: {before.id}")
        embed.add_field(name=f'User: ', value=f'{before.author.mention}', inline=False)
        embed.add_field(name='Before:', value=f"{before.content}", inline=False)
        embed.add_field(name="After:", value=f"{after.content}", inline=False)
        channel = discord.utils.get(guild.channels, name='message-logs')
        await channel.send(embed=embed)




    @commands.Cog.listener()
    async def on_message_delete(self, message):
        guild = message.guild
        embdel = discord.Embed(
        title='User Message deleted', color=0x982abc
        )
        embdel.set_author(name='Subaru')
        embdel.add_field(name=f'User:', value=f'{message.author.mention}')
        embdel.add_field(name='message deleted', value=message.content)
        channel = discord.utils.get(guild.channels, name='message-logs')
        await channel.send(embed=embdel)




    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        embmsg = discord.Embed(
        title='User joined:', color=0x982abc
        )
        embmsg.set_author(name="Subaru")
        embmsg.add_field(name='User: ', value=f"{member.mention}(ID: {member.id}) account age: {member.created_at}", inline=False)
        channel = discord.utils.get(guild.channels, name='member-logs')
        await channel.send(embed=embmsg)




    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        embmsg1 = discord.Embed(
        title='User left:', color=0x982abc
        )
        embmsg1.set_author(name="Subaru")
        embmsg1.add_field(name=f'User: ', value=f'{member.mention} (ID: {member.id})', inline=False)
        channel = discord.utils.get(guild.channels, name='member-logs')
        await channel.send(embed=embmsg1)





def setup(client):
    client.add_cog(Logging(client))
