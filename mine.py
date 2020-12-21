import discord

client = discord.Client(self_bot = True)

TOKEN = "NTEzMzUxOTE3NDgxNjIzNTcy.X-A8YA.VqQg4sPCwuph4oCctg-NTGhfYHA"


@client.event
async def on_ready():
    activity=discord.Game(name="Test.py.exe")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f"ready! {client.user.name}")

client.run(TOKEN, bot=False)
