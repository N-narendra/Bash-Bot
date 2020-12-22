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
        embed.add_field(name = "Date Of Join", value = member.joined_at.__format__('%A %d %B %Y at %H:%M'), inline = False)
        embed.add_field(name = "Account Created At", value = member.created_at.__format__('%A %d %B %Y at %H:%M'), inline = False)
        embed.add_field(name = "Roles", value = ([r.mention for r in member.roles[1:]]), inline = False)
        embed.add_field(name = "Status", value = member.status, inline = False)
        embed.add_field(name = "Username", value = member.nick, inline = False)
        embed.add_field(name = "High Role", value = member.top_role.mention,inline = False)
        embed.set_thumbnail(url= member.avatar_url)
        embed.set_footer(icon_url= ctx.author.avatar_url, text=f"Command Executed By {ctx.message.author.name}")
        await ctx.message.delete()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Whois(client))

