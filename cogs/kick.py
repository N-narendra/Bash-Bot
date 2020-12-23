import discord
from discord.ext import commands

class Rm(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(help="rm Is commands Which To Remove Member from Server..!")
    @commands.has_permissions(kick_members = True )
    async def rm(self, ctx,member : discord.Member,*,reason=None):
        guild = ctx.guild
        if (member) == (ctx.message.author):
            await ctx.send(f'**{ctx.message.author.name},** you can\'t Remove yourself, ¯\_(ツ)_/¯.')
            return
        try:
            await member.send(f" you have been Banned from: **{guild.name}** reason: **{reason}**")
            await member.kick(reason=reason)
            embed = discord.Embed(title="Removed", description=f"{member.mention} was Removed ", colour=discord.Colour.green())
            embed.add_field(name="reason:", value=reason, inline=False)
            await ctx.send(embed=embed)
            await member.kick(reason=reason)
        except:
            await ctx.send("**The Members Has thier dms Closed.!**\n")
            embed = discord.Embed(title="Removed", description=f"{member.mention} was Removed ", colour=discord.Colour.green())
            embed.add_field(name="reason:", value=reason, inline=False)
            await ctx.send(embed=embed)
            await member.kick(reason=reason)
def setup(client):
    client.add_cog(Rm(client))