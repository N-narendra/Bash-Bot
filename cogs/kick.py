import discord
from discord.ext import commands

class Rm(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(help="rm Is commands Which To Remove Member from Server..!")
    @commands.has_permissions(kick_members = True )
    async def rm(self, ctx,member : discord.Member,*,reason):
       if member == ctx.message.author:
        await ctx.send(
            f'**{ctx.message.author.name},** you can\'t Remove yourself, ¯\_(ツ)_/¯.')
        return
        try:
            await member.send("``you Have Removed,Because:`` " +reason)
            await member.kick(reason=reason)
        except:
            await ctx.send("The Members Has thier dms Closed.!\n")
            await ctx.channel.send(member.name +"`` Have been Removed,Because: ``"+ reason)
            await member.kick(reason=reason)
def setup(client):
    client.add_cog(Rm(client))