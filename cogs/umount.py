import discord
from discord.ext import commands

class Umount(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
    async def umount(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="umount", description=f"**{member.mention}** was umount ", colour=discord.Colour.red())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" you have been umount from: **{guild.name}** reason: **{reason}**")


def setup(client):
    client.add_cog(Umount(client))

