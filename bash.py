import discord
from discord.ext import commands


client = commands.Bot(command_prefix="$")

filtered_words = ["fuck","shit","bitch"]

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.online, activity = discord.Game("$help"))
    print("I am online")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you Can't Do That :( ")
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please Enter All Arguments..!")
        await ctx.message.delete()   
    else: 
        raise error   
    
@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()
        await client.process_commands(msg)
        break

@client.command(help="(show author_name)")
async def whoami(ctx) :
    await ctx.send(f"```You are {ctx.message.author.name}..!```")

@client.command(help="Ping Helps To Show Network letency..!")
async def ping(ctx) :
     await ctx.send(f'"🏓 Pong with {round(client.latency * 100)} ms')

@client.command(help="Help To Clear Chats")
@commands.has_permissions(manage_messages = True )
async def clear(ctx, amount=1) :
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f"Message Cleared By {ctx.message.author.name}..!")

@client.command(help="Print args....!")
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)
 
@client.command(help="rm Is commands Which To Remove Member from Server..!")
@commands.has_permissions(kick_members = True )
async def rm(ctx,member : discord.Member,*,reason):
    try:
        await member.send("`` you Have Removed,Because:``" +reason)
        await member.kick(reason=reason)
    except:
        await ctx.send("The Members Has thier dms Closed.!\n")
        await ctx.channel.send(member.name +"`` Have been Removed,Because: ``"+ reason)
        await member.kick(reason=reason)


@client.command(help="Ban Helps To Ban Members From Server..!")
@commands.has_permissions(ban_members = True )
async def ban(ctx,member : discord.Member,*,reason):
     await ctx.channel.send(member.name +"`` Have been Banned,Because: ``"+reason)
     await member.send("`` you Have Banned,Because:`` "+reason)
     await member.ban(reason=reason)

@client.command(help="help To Unban Members..!")
@commands.has_permissions(ban_members=True) 
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user 

        if (user.name, user.discriminator)==(member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name +" has Been Unbanned...!")
            return

            await ctx.send(member+" was not found..!")

@client.command(help="Helps To Memeber to Mute From Server")
@commands.has_permissions(kick_members=True)
async def umount(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(788064278527475712)

    await member.add_roles(muted_role)
    await ctx.send(member.mention + "Has Been Unmounted")

@client.command(help="helps To unmute From Server..!")
@commands.has_permissions(kick_members=True)
async def mount(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(788064278527475712)

    await member.remove_roles(muted_role)
    await ctx.send(member.mention + "Has Been mounted")
   

client.run("Nzg5NTA0OTg0NzUyMDYyNDg2.X9zB0A.nORPkFLfgmVz22C47lcU5Fl8LDc")  
