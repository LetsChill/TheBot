#might make a tut on how to add commands
import discord
from discord.ext import commands

TOKEN = "TOKEN"

client = commands.AutoShardedBot(command_prefix="?")

#cogs loader
for filename in os.listdir('./cogs'):
        if filename.endswith(".py") and not filename.startswith("_"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print("Cogs Loaded!")


client.run(TOKEN)
