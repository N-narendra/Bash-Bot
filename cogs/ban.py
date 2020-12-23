import discord
from discord.ext import commands

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="Ban Helps To Ban Members From Server..!")
    @commands.has_permissions(ban_members = True )
    async def ban(self, ctx,member : discord.Member,*,reason=None):
       
        guild = ctx.guild

        embed = discord.Embed(title="Banned", description=f"{member.mention} was Banned ", colour=discord.Colour.green())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.send(f" you have been Banned from: {guild.name} reason: {reason}")
        await member.ban(reason=reason)

   
def setup(client):
    client.add_cog(Ban(client))