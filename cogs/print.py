import discord
from discord.ext import commands

class Print(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(help="Print args....!")
    async def print(self,ctx, *args):
	    response = ""

	    for arg in args:
		    response = response + " " + arg

	    await ctx.channel.send(response)

def setup(client):
    client.add_cog(Print(client))

