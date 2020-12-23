import discord
from discord.ext import commands

class About(commands.Cog):

    def __init__(self, client):
        self.client = client
      

    @commands.command(help="About Bot..!")
    async def about(self, ctx) :
        em = discord.Embed(title = "BashBot", description="**About me**\n\n"
                       "**BashBot is a Discord bot that allows Commands access via chat It will like Binaries.**\n\n"
                       "**Discord**: [Click Here](https://discord.gg/XAGcbun)\n\n"
                       "**BASHBOT Invite**: [Click Here](https://discord.com/api/oauth2/authorize?client_id=789504984752062486&permissions=8&scope=bot)\n\n"
                       "**Author**: **Narendra**",colour=discord.Colour.red())
        em.set_footer(icon_url= ctx.author.avatar_url, text=f"Command Executed By {ctx.message.author.name}")
     
        await ctx.send(embed = em)
           


def setup(client):
    client.add_cog(About(client))



      

   
