import discord
from discord.ext import commands

class Mount(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="helps To unmute From Server..!")
    @commands.has_permissions(kick_members=True)
    async def mount(self, ctx,member : discord.Member):
         muted_role = ctx.guild.get_role(790526327069212692)

         await member.remove_roles(muted_role)
         await ctx.send(member.mention + "Has Been mounted")

def setup(client):
    client.add_cog(Mount(client))

