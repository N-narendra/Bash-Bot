import discord
import os 
import datetime
import random
import asyncio
import json 
from discord.ext import commands

client = commands.Bot(command_prefix= "$")
client.remove_command("help")

@client.event
async def on_ready() :
    await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} Servers | $help"))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Youtube"))
    
async def ch_pr():
        await client.wait_until_ready()

        statuses = ["CyberPunk 2088", f"on {len(client.guilds)} Servers | $help",]

        while not client.is_closed():

            status = random.choice(statuses)

            await client.change_presence(activity=discord.Game(name=status))

            await asyncio.sleep(10)


client.loop.create_task(ch_pr())         



filtered_words = ["fuck","shit","bitch","fucker"]

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()


    await client.process_commands(msg)


@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Invaild Command Type $help..!")
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("**You Dont Have Permissions..!**")
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("**Please Enter All Arguments..!**")
        await ctx.message.delete()   
    else: 
        raise error   
    
@client.command(help="Load Basically Helps Fix Commands where Looping..!")
@commands.has_permissions(kick_members = True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command(help="Unload Helps in Unload Commands Unstable use..! ")
@commands.has_permissions(kick_members = True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')   


#client.run("NzkwNDgwODk1MTI3MTkxNTUz.X-BOsw.50pGDsZ4m48yY7Whl2vhAd4wyLM")  
client.run("Nzg5NTA0OTg0NzUyMDYyNDg2.X9zB0A.nORPkFLfgmVz22C47lcU5Fl8LDc") 

