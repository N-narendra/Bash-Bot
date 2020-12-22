import discord
import random
from discord.ext import commands

class Bash(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="You Can Play Guess Game With Bash $bash Your Questions.")
    async def bash(self, ctx, *, question):
        responses = ['yes','no','Maybe','Not Sure','Sure','Hmm','lol','As I see it, yes','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don’t count on it','It is certain','It is decidedly so','Most likely','My reply is no','My sources say no','Outlook good','Outlook not so good','Reply hazy try again','Signs point to yes','Very doubtful','Without a doubt','Yes, definitely','You may rely on it']   
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

def setup(client):
    client.add_cog(Bash(client))

