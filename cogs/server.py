import discord
from discord.ext import commands


class Server(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    async def create(self, ctx):
                category = await guild.create_cate
        guild = ctx.guild
        category = await guild.create_category("Text Channel")
        await ctx.send("creating the server atm")
        await guild.create_text_channel("general┃💭", category=category)
        
def setup(client):
    client.add_cog(Server(client))