import discord
from discord.ext import commands

class Whoami(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
      print("bash_bot is online.")
      

    @commands.command(help="show Client Name")
    async def whoami(self, ctx) :
        await ctx.send(f"```You are {ctx.message.author.name}..!```")


def setup(client):
    client.add_cog(Whoami(client))

