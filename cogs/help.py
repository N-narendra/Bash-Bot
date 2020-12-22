import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title= "**Help**", description = "**Help give Usage of Commands**",colour= discord.Colour.dark_orange())

        em.add_field(name = "**Commands**", value= "Rm,Ban,Unban\nPrefix,Mount,Umount\nClear.",inline=True)
        em.add_field(name= "**Network**",  value="Ping",inline=False)
        em.add_field(name= "**Misc**",  value="Whoami\nWhois",inline=True)
        em.add_field(name= "**Fun**",  value="Bash",inline=False)
        em.add_field(name= "**About**",  value="About",inline=False)
        em.add_field(name= "**More Help**",  value="**$Help <command>**\n",inline=False)
        em.set_footer(icon_url= ctx.author.avatar_url, text=f"Command Executed By {ctx.message.author.name}")

        await ctx.send(embed = em)

def setup(client):
    client.add_cog(Help(client))
