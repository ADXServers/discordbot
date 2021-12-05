import discord
import os
from datetime import datetime
client = discord.Client()
prefix = "a!"
version = "1.2.0"
author = "ADX#5452"
mapversion = "1.0.0"

now = datetime.now()

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
            await channel.send_message(f"{member.mention}Welcome to :ice_cube: ICE NETWORK :ice_cube:")
@client.event
async def on_message(message):
    global said
    msgscore = 0
    id = client.get_guild(870007912452468746)
    censored = ["nigger", "nigga", "nig", "n i g", "test", "t e s", "tes"]
    mapcmd = ["map", "workshop"]
    infocmds = ["info", "about", "bot"]
    ping = ["@ADX", "<@917078593429987389>", "@917078593429987389", "<@ADX>"]
    modcmds = ["workshop", "mod", "mods"]
    assetcmd = ["missing critical assets", "missing vehicle assets", "missing assets", "assets", "asset" , "this server is using modified version of the map", "Asset"]
    if os.path.exists("/home/sami/Desktop/vsc/discord/log.txt") == False:
        file = open("log.txt", "w")
        file.close() 
    if os.path.exists("/home/sami/Desktop/vsc/discord/score"+message.author.mention+".txt") == False:
        file = open("score"+message.author.mention+".txt", "w")
        file.close()
    else:
        file = open("score"+message.author.mention+".txt", "r")
        msgscore = int(file.read())
        file.close()
    msgscore +=1
    file = open("score"+message.author.mention+".txt", "w")
    file.write(str(msgscore))
    file.close()

    if message.content.lower() in ping:
        await message.channel.send(f"Hi {message.author.mention}, how may I help you?")


    if str(message.channel) == "💻┃bot-cmd" or "staff-cmds":
        if message.content.lower() == prefix+"usercount":
            #await message.channel.send("Members: "+str(id.member_count))
            embed = discord.Embed(title="Members", description=f"{id.member_count}", colour=0x00FF00)
            await message.channel.send(content=None, embed=embed)

    if any([x for x in message.content.lower().split() if x in censored]):
        await message.channel.purge(limit=1)
        embed = discord.Embed(title="Censored word was removed and logged", description=f"Sender: {message.author.mention}", colour=0xFF0000)
        print(f"{current_time} : {message.author.mention} : {message.content} : {message.channel}")
        await message.channel.send(content=None, embed=embed)
        file = open("log.txt", "a")
        file.write(f"{current_time} : {message.author.mention} : {message.content} : {message.channel}\n")



    if str(message.channel) == "❓┃community-support" or "staff-cmds":
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



    if str(message.channel) == "❓┃community-support" or "staff-cmds":
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

    if str(message.channel) == "❓┃community-support" or "staff-cmds":
        if os.path.exists(path+cmd) == False:
            if any([x for x in message.content.lower().split() if x in infocmds]):
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


    if str(message.channel) == "❓┃community-support" or "staff-cmds":
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

    if message.content.lower() == prefix+"levelup":
        file = open("score"+message.author.mention+".txt", "r")
        if int(file.read()) > 999:
            print("debug")
    

client.run("no bich")