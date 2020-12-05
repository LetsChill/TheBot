import discord
from discord.ext import commands


class Server(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command()
    @commands.cooldown(1, 1000, commands.BucketType.guild)
    @commands.has_any_role("Owner")
    async def create(self, ctx):
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
        
        ancat = await guild.create_category("Welcome")
        
        txtcat = await guild.create_category("text channels")
        
        givcat = await guild.create_category("giveaways")
        
        stfcat = await guild.create_category("staff chat")
        
        await guild.create_text_channel("general┃💭", category=txtcat)
        await guild.create_text_channel("check-invites┃🎟", category=txtcat)
        
        await guild.create_text_channel("invite-tracker┃🧭", category=ancat)
        await guild.create_text_channel("announcements┃📢", category=ancat)
        await guild.create_text_channel("rules┃📖", category=ancat)
        await guild.create_text_channel("make-a-ticket┃🎫", category=ancat)
        
        await guild.create_text_channel("giveaway┃1", category=givcat)
        await guild.create_text_channel("giveaway┃2", category=givcat)
        await guild.create_text_channel("giveaway┃3", category=givcat)
        await guild.create_text_channel("proofs┃☑️", category=givcat)
        
        await guild.create_text_channel("staff-chat", category=stfcat)
        await guild.create_text_channel("staff-commands", category=stfcat)
        await guild.create_text_channel("accounts", category=stfcat)
        
def setup(client):
    client.add_cog(Server(client))