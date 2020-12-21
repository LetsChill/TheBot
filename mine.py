import discord

client = discord.Client()

TOKEN = "NTEzMzUxOTE3NDgxNjIzNTcy.X9Yziw.bp_cWSzIE1YaLKNlmR3H8-pQBE"


@client.event
async def on_ready():
    activity=discord.Game(name="a game")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f"ready! {client.user.name}")

client.run(TOKEN)
