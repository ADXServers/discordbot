import discord
import os
from datetime import datetime
from discord.ext import commands
from discord.utils import get
bot = commands.Bot(command_prefix='a!')

from discord.audit_logs import AuditLogDiff

client = discord.Client()
prefix = "a!"
version = "1.2.0"
author = "ADX#5452"
mapversion = "1.0.0"
now = datetime.now()
file = open("words.txt", "r")
print(file.read().split())

current_time = now.strftime("%H:%M:%S")
print("Time : "+ current_time)
path = "/home/sami/Desktop/vsc/discord/"

cmd = "info"
answer = "Author: "+author+"\nVersion: "+version+"\nPrefix: "+prefix
cmd2 = "asset"


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel == "870008898352975874":
            await channel.send_message(f"{member.mention} Welcome to :ice_cube: ICE NETWORK :ice_cube:")
@client.event
async def on_message(message):
    global said
    msgscore = 0
    level = 0
    id = client.get_guild(870007912452468746)
    helpchannels = ["staff-cmds", "❓┃community-support"]
    mapcmd = ["map", "workshop"]
    infocmds = ["info", "about", "bot"]
    ping = ["@ADX", "<@917078593429987389>", "@917078593429987389", "<@ADX>"]
    modcmds = ["workshop", "mod", "mods"]
    assetcmd = ["missing critical assets", "missing vehicle assets", "missing assets", "assets", "asset" , "this server is using modified version of the map", "Asset"]
    usrs = ["ADX#5452", "Peb#2320"]
    if os.path.exists(path+"words.txt") == False:
        file = open("words.txt", "w")
        file.close()
    if os.path.exists("/home/sami/Desktop/vsc/discord/log.txt") == False:
        file = open("log.txt", "w")
        file.close()
    if os.path.exists(path+"level"+message.author.mention+".txt") == False:
    #    file = open("level"+message.author.mention+".txt", "w")
    #    file.close()
        templevel = 0
    else:
        file = open("level"+message.author.mention+".txt", "r")
        templevel = file.read()
        templevel = int(templevel)
        member = message.author
        role = discord.utils.get(member.guild.roles, name="epic")
        if templevel >= 0:
            level = templevel

        else:
            level = 0
            file.close()
            file = open("level"+message.author.mention+".txt", "w")
            file.write(str(level))
        file.close()

    if os.path.exists("/home/sami/Desktop/vsc/discord/score"+message.author.mention+".txt") == False:
        file = open("score"+message.author.mention+".txt", "w")
        file.write("0")
        file.close()
    else:
        file = open("score"+message.author.mention+".txt", "r")

        msgscore = int(file.read())
        file.close()
    file = open("words.txt", "r")
    if str(message.content.lower()) not in file.read():
        msgscore +=1
        file = open("score"+message.author.mention+".txt", "w")
        file.write(str(msgscore))
        file.close()

    if message.content.lower() in ping:
        await message.channel.send(f"Hi {message.author.mention}, how may I help you?")


    if str(message.channel) == "💻┃bot-cmd":
        if message.content.lower() == prefix+"usercount":
            #await message.channel.send("Members: "+str(id.member_count))
            embed = discord.Embed(title="Members", description=f"{id.member_count}", colour=0x00FF00)
            await message.channel.send(content=None, embed=embed)
    #else:
    #    file = open("words.txt", "r")
    #    print(file.read())
    if str(message.channel) == "words":
        if str(message.author) in usrs:
            await message.channel.purge(limit=1)
            file = open("words.txt", "r")
            if message.content.lower() not in file.read():
                file = open("words.txt", "a")
                file.write(message.content.lower()+"\n")
                file.close()
                #censored.append(message.content.lower())
                print(message.content.lower()+" was added to censored words.")
                embed = discord.Embed(title=message.content.lower()+" was added to censored words.", description=message.author.mention, colour=0xFF0000)
                await message.channel.send(content=None, embed=embed)


    if str(message.channel) != "words":
        file = open("words.txt", "r")
        if any([x for x in message.content.lower().split() if x in file.read().split()]):
            await message.channel.purge(limit=1)
            embed = discord.Embed(title="Censored word was removed and logged", description=f"Sender: {message.author.mention}", colour=0xFF0000)
            print(f"{current_time} : {message.author.mention} : {message.content} : {message.channel}")
            await message.channel.send(content=None, embed=embed)
            file = open("log.txt", "a")
            file.write(f"{current_time} : {message.author.mention} : {message.content} : {message.channel}\n")



    if str(message.channel) in helpchannels or "ticket" in str(message.channel):
        if os.path.exists(path+"mod") == False:
            if any([x for x in message.content.lower().split() if x in modcmds]):
                #await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
                embed = discord.Embed(title="Ice Network's Workshop Collection", description="Find all mods used by ICE RP", colour=0x0000FF)
                embed.add_field(name="Workshop", value="https://steamcommunity.com/sharedfiles/filedetails/?id=2669939420")
                await message.channel.send(content=None, embed=embed)
                file = open("mod", "w")
                file.write("f")
                file.close()            

        if os.path.exists(path+"mod") == True:
            os.system("rm "+path+"mod")



    if str(message.channel) in helpchannels or "ticket" in str(message.channel):
        if os.path.exists(path+"map") == False:
            if any([x for x in message.content.lower().split() if x in mapcmd]):
                #await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
                embed = discord.Embed(title="Ice Network's RP Map", description="Version: 1.0.0", colour=0x00FFFF)
                embed.add_field(name="Creator", value="Comarco")
                embed.add_field(name="Workshop", value="https://steamcommunity.com/sharedfiles/filedetails/?id=2653670482")
                await message.channel.send(content=None, embed=embed)
                file = open("map", "w")
                file.write("f")
                file.close()            

        if os.path.exists(path+"map") == True:
            os.system("rm "+path+"map")


    #var

    if str(message.channel) in helpchannels or "ticket" in str(message.channel):
        if os.path.exists(path+cmd) == False:
            if message.content.lower() == prefix+"info":
                #await message.channel.send(answer)
                embed = discord.Embed(colour= 0xFF00FF)
                embed.add_field(name="Version", value=version)
                embed.add_field(name="Author", value=author)
                embed.add_field(name="Prefix", value=prefix)
                #await reply(content=None, embed=embed)  
                await message.channel.send(content=None, embed=embed)
                file = open(cmd, "w")
                file.write(cmd)
                file.close()            

        if os.path.exists(path+cmd) == True:
            os.system("rm "+path+cmd)


    if str(message.channel) in helpchannels or "ticket" in str(message.channel):
        if os.path.exists(path+cmd2) == False:
            if any([x for x in message.content.lower().split() if x in assetcmd]):
                #await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
                embed = discord.Embed(title="Solutions for your problem", description="Missing Assets", colour=0xFF0000)
                embed.add_field(name="Subscribe to our workshop content here", value="https://steamcommunity.com/sharedfiles/filedetails/?id=2669939420")
                embed.add_field(name="Remove all workshop mods in folder", value="/steamapps/workshop/content/304930")
                await message.channel.send(content=None, embed=embed)
                file = open(cmd2, "w")
                file.write("f")
                file.close()            

        if os.path.exists(path+cmd2) == True:
            os.system("rm "+path+cmd2)

    file = open("score"+message.author.mention+".txt", "r")
    if int(file.read()) >= 20:
        msgscore = 0
        level += 1
        file = open("level"+message.author.mention+".txt", "w")
        file.write(str(level))
        file.close()
        embed = discord.Embed(title="Levelup!", description=message.author.mention, colour=0xFF00FF)
        file = open("level"+message.author.mention+".txt", "r")
        embed.add_field(name="Level", value=file.read())
        file.close()
        file = open("score"+message.author.mention+".txt", "w")
        file.write(str(msgscore))
        await message.channel.send(content=None, embed=embed)
    file.close()
    if os.path.exists(path+"score"+message.author.mention+".txt") == True:
        if os.path.exists(path+"level"+message.author.mention+".txt") == True:
            if int(level) == 50 and int(msgscore) == 0:
                embed = discord.Embed(title="Someone reached the level 50 and got EPIC rank", description=message.author.mention)
                embed.add_field(name="Rank", value="<@917394211018522624>")
                embed.add_field(name="Level", value=str(level))
                await message.channel.send(content=None, embed=embed)
                await member.add_roles(role)

    if prefix+"purge" in message.content.lower():
        if message.author.guild_permissions.manage_messages:
            arg = message.content.lower().split()
            if len(arg) <= 1:
                embed = discord.Embed(title="Usage: a!purge <messages(int)>", description=message.author.mention, color=0xFF0000)
                await message.channel.send(content=None, embed=embed)
            elif len(arg) >= 3:
                embed = discord.Embed(title="Usage: a!purge <messages(int)>", description=message.author.mention, color=0xFF0000)
                await message.channel.send(content=None, embed=embed)
            else:
                await message.channel.purge(limit=int(arg[1]))
                embed = discord.Embed(title="Messages purged", description=str(arg[1]))
                embed.add_field(name="Executed by", value=message.author.mention)
                await message.channel.send(content=None, embed=embed)
        else:
            embed = discord.Embed(title="Missing Permissions", description=message.author.mention, color=0xFF0000)
            embed.add_field(name="Permission", value="manage_messages")
            await message.channel.send(content=None, embed=embed)
    if prefix+"help" in message.content.lower():
        embed = discord.Embed(title="Commands", description=message.author.mention, color=0xFF000)
        embed.add_field(name="a!help", value="usage: a!info")
        embed.add_field(name="a!info", value="usage: a!info")
        embed.add_field(name="a!purge <admin only>", value="usage: a!purge <messages(int)>")
        embed.add_field(name="a!level", value="usage: a!level")
        #embed.add_field(name="a!setlevel <admin only>", value="usage: a!givelevel <level(int)>")
        await message.channel.send(content=None, embed=embed)
    #if prefix+"setlevel" in message.content.lower():
        #if message.author.guild_permissions.administrator:
            #arg = message.content.lower().split()
            #if len(arg) <= 1:
                #embed = discord.Embed(title="Usage: a!setlevel <level(int)>", description=message.author.mention, color=0xFF0000)
                #await message.channel.send(content=None, embed=embed)
            #if len(arg) >= 3:
                #embed = discord.Embed(title="Usage: a!setlevel <level(int)>", description=message.author.mention, color=0xFF0000)
                #await message.channel.send(content=None, embed=embed)
            #else:
                #if os.path.exists(path+"level"+message.author.mention+".txt") == True:
                    #file = open("level"+message.author.mention+".txt", "w")
                    #arg[1] = int(arg[1])
                    #file.write(str(arg[1]))
                    #embed = discord.Embed(title="Level changed", description=message.author.mention, color=0xFF000)
                    #embed.add_field(name="Level", value=arg[1])
                    #await message.channel.send(content=None, embed=embed)
client.run("no")