import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title= "**Help**", description = "**Help give Usage of Commands**",colour= discord.Colour.dark_orange())
        em.add_field(name= "**Rm**",  value="**syntax:- $rm <@member> <reason>.**\n",inline=False)
        em.add_field(name= "**Ban**",  value="**syntax:-$ban <@member> <reason>.**\n",inline=False)
        em.add_field(name= "**Unban**",  value="**syntax:- $unban <member#0000> <reason>.**\n",inline=False)
        em.add_field(name= "**Mount(unmute)**",  value="**syntax:- $mount <@member>**\n",inline=False)
        em.add_field(name= "**Umount(mute)**",  value="**syntax:- $umount <@member>**\n",inline=False)
        em.add_field(name= "**Clear**",  value="**syntax:- $clear <value>**\n",inline=False)
        em.add_field(name= "**Prefix(soon)**",  value="**syntax:- $prefix <new prefix>**\n",inline=False)
        em.add_field(name= "**Load**",  value="**syntax:- $load <command>**\n",inline=False)
        em.add_field(name= "**Unload**",  value="**syntax:- $unload <command>**\n",inline=False)
        em.add_field(name= "**Print**",  value="**syntax:- $print <args>**\n",inline=False)
        em.add_field(name= "**Whoami**",  value="**syntax:- $whoami**\n",inline=False)
        em.add_field(name= "**Whois**",  value="**syntax:- $whois <@member>**\n",inline=False)
        em.add_field(name= "**Bash**",  value="**syntax:- $Bash <questions>**\n",inline=False)

        em.set_footer(icon_url= ctx.author.avatar_url, text=f"Command Executed By {ctx.message.author.name}")

        await ctx.send(embed = em)

def setup(client):
    client.add_cog(Help(client))
