import discord
import os 
from discord.ext import commands


client = commands.Bot(command_prefix="$")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.online, activity = discord.Game("$help"))


filtered_words = ["fuck","shit","bitch","fucker","noob"]

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()


    await client.process_commands(msg)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you Can't Do That :( ")
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please Enter All Arguments..!")
        await ctx.message.delete()   
    else: 
        raise error   
    

@client.command(help="Load Basically Helps Fix Commands where Looping..!")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command(help="Unload Helps in Unload Commands Unstable use..! ")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')    

#beta#client.run("NzkwNDgwODk1MTI3MTkxNTUz.X-BOsw.50pGDsZ4m48yY7Whl2vhAd4wyLM")  
client.run("Nzg5NTA0OTg0NzUyMDYyNDg2.X9zB0A.nORPkFLfgmVz22C47lcU5Fl8LDc") 

