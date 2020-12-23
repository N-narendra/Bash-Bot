import discord
from discord.ext import commands
import random

class Bad(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            msg = message
            guild = message.guild
            gold = discord.Color.dark_gold()
            bad_list = ["fuck",
                        "bitch",
                        "slut",
                        "dick",
                        "ass",
                        "dike",
                        "cunt",
                        "pussy",
                        "nigger",
                        "kkk",
                        "negro",
                        "cracka",
                        "jew",
                        "honkie"]
            responses = ["Stop it Get Some Help..!",
                         ".....some people these days..... need to good switch to the [REDACTED]",
                         "Who taught you to use such filthy language?!?",
                         "Oh yes, talk dirty to me....",
                         "You FILTHY CASUAL! You need to learn better swears!",
                         "You're choice in words is reassuring. I know that you will never be anything now.",
                         "FUCK! Another one slipped through! GRAB THE RAID!",
                         "SHIT! SHIT! WE GOT ONE! WE FINALLY GOT ONE! GET THE HAMMER!"]
            for bad_word in bad_list:
                if bad_word in message.content:
                    response = random.choice(responses)
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="⚠", value=c_r, inline=False)
                    embed.set_thumbnail(url=self.client.user.avatar_url)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.send(embed=embed)
                    return
def setup(client):
    client.add_cog(Bad(client))

