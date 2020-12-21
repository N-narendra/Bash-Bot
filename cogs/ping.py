import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="Ping Helps To Show Network letency..!")
    async def ping(self, ctx):
        await ctx.send(f'"🏓 Pong with {round(self.client.latency * 100)} ms')

def setup(client):
    client.add_cog(Ping(client))

