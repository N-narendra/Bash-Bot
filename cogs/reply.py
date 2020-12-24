import discord
from discord.ext import commands
import random

class Reply(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @commands.Cog.listener()
    async def on_message(self,message):
        if not message.author.bot:
            msg = message
            guild = message.guild
            gold = discord.Color.dark_gold()
            rs = (message.content.lower())
            if rs == ("goodnight"):
                    response = ("Goodnight Buddy..!")
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="😴", value=c_r, inline=True)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.send(embed=embed)
                    return
                    rs ==(message.content.lower())    
            elif rs == ("goodmorning"):
                    response = ("GoodMorning Buddy..!")
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="☕", value=c_r, inline=True)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.send(embed=embed)
                    return
                    rs ==(message.content.lower())
            elif rs == ("gm"):
                    response = ("GoodMorning Buddy..!")
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="☕", value=c_r, inline=True)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.send(embed=embed)
                    return
                    rs ==(message.content.lower()) 
            elif rs == ("gn"):
                    response = ("GoodNight Buddy..!")
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="😴", value=c_r, inline=True)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.send(embed=embed)
                    return
                    rs ==(message.content.lower())
            elif rs == ("good morning"):
                    response = ("Good Morning Buddy..!")
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="☕", value=c_r, inline=True)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.send(embed=embed)
                    return
                    rs ==(message.content.lower())
            elif rs == ("good night"):
                    response = ("Good Night Buddy..!")
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="😴", value=c_r, inline=True)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.send(embed=embed)
                    return                               
                      
def setup(client):
    client.add_cog(Reply(client))

