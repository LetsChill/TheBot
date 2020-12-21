import discord

client = discord.Client()

TOKEN = "NTEzMzUxOTE3NDgxNjIzNTcy.X-A6lQ.w15VyhN5ffRGikxDpA0HgbY4orc"


@client.event
async def on_ready():
    activity=discord.Game(name="Test.py.exe")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f"ready! {client.user.name}")

client.run(TOKEN)
