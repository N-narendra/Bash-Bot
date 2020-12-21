import discord
from discord.ext import commands

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="Ban Helps To Ban Members From Server..!")
    @commands.has_permissions(ban_members = True )
    async def ban(self, ctx,member : discord.Member,*,reason):
       

        await ctx.channel.send(member.name +"`` Have been Banned,Because:`` "+reason)
        await member.send("``you Have Banned,Because:`` "+reason)
        await member.ban(reason=reason)

   
def setup(client):
    client.add_cog(Ban(client))