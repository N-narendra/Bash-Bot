import discord
from discord.ext import commands

class About(commands.Cog):

    def __init__(self, client):
        self.client = client
      

    @commands.command(help="About Bot..!")
    async def about(self, ctx) :
         await ctx.send("__**About me**__\n"
                       "BashBot is a Discord bot that allows Commands access via chat It will like Binaries.\n"
                       "**Discord**: https://discord.gg/XAGcbun\n"
                       "**Author**: Narendra.")


def setup(client):
    client.add_cog(About(client))



      

   
