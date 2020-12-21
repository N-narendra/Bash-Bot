import discord
from discord.ext import commands

class Whois(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(help="Helps To Show User Info..!")
    @commands.has_permissions(kick_members=True)
    async def whois(self, ctx, member : discord.Member):
        embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.dark_magenta())
        embed.add_field(name = "ID", value = member.id, inline = True)
        embed.set_thumbnail(url= member.avatar_url)
        embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Command Executed By {ctx.message.author.name}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Whois(client))

