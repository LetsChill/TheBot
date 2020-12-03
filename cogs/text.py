import discord
from discord.ext import commands

class Text(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(ctx)
    async def donate():
        dembed=discord.Embed(
        title="Donate me!", description="http://paypal.me/LetsChiLI", color=0x7a219e 
        )
        await ctx.send(embed=dembed)
        
        
        
        
        
def setup(client):
    client.add_cog(Text(client))