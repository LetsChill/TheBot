import discord
import os
import datetime
import asyncio
import random
from discord.ext import commands

intents = discord.Intents(members=True)

TOKEN = os.getenv("TOKEN")

welcomechannel = await client.fetch_channel(776751235679780894)

newUserMessage = ""

client = commands.Bot(command_prefix = ':')

@client.event
async def on_ready():
	print("The bot is up!")
	print(client.user)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Servers :help'))

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    try: 
        await client.send_message(member, newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)
    embed=discord.Embed(
        title="Welcome "+member.name+"!"
        description="We're so glad you're here!"
        color=discord.Color.green()
    )
        
    role = discord.utils.get(member.server.roles, name="name-of-your-role") #  Gets the member role as a `role` object
    await client.add_roles(online, role) # Gives the role to the user
    print("Added role '" + role.name + "' to " + member.name)

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
    embed=discord.Embed(
        title="😢 Goodbye "+member.name+"!",
        description="Until we meet again old friend." # A description isn't necessary, you can delete this line if you don't want a description.
        color=discord.Color.red() # There are lots of colors, you can check them here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
    )

@client.command()
@commands.has_role("Giveaways")
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 

    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} mintues from now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")


def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]


@client.command()
@commands.has_role("Giveaways")
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

    questions = ["Which channel should it be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}!")

@client.command()
@commands.has_any_role("clear perms", "Admin")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
     
    await member.kick()
    await context.send('User ' + member.mention + ' has been kicked')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.Member):
     
    await member.ban()
    await context.send('User ' + member.mention + ' has been banned')

@client.event()
async def on_member_join(member):
    channel_send(f"Welcome {member.mention} to our server!)



if __name__ == "__main__":
    client.run(TOKEN)

