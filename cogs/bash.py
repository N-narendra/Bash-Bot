import discord
import random
from discord.ext import commands

class Bash(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="You Can Play Guess Game With Bash $bash Your Questions.")
    async def bash(self, ctx, *, question):
        responses = ['yes','no','Maybe','Not Sure','Sure','Hmm','lol','Heheboi','wth']   
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

def setup(client):
    client.add_cog(Bash(client))

