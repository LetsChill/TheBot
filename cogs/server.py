import discord
from discord.ext import commands


class Server(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    async def create(self, ctx):
        guild = ctx.guild
        await ctx.send("creating the server atm")
        await  guild.create_category("Text Channels")
        
        await guild.create_text_channel("general┃💭", category="Text Channels")
        
def setup(client):
    client.add_cog(Server(client))