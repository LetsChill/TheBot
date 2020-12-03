import discord
from discord.exr import commands

class Text(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(self, ctx)
    async def donate():
        dembed = discord.Embed(
        title="Buy Me a cake and make my day!"
        description="http://paypal.me/LetsChiLI", color=0x982abc
        )
        await ctx.send(dembed=embed)
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def setup(client):
    client.add_cog(Text(client))