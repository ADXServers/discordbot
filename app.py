import discord
import os
client = discord.Client()
prefix = "a!"
version = "1.0.0"
author = "ADX#5452"

path = "/home/sami/Desktop/vsc/discord/"

cmd = "info"
answer = "Author: "+author+"\nVersion: "+version+"\nPrefix: "+prefix

cmd2 = "asset"

@client.event
async def on_message(message):
    global said
    id = client.get_guild(870007912452468746)
    ping = ["@ADX", "<@917078593429987389>", "@917078593429987389", "<@ADX>"]
    modcmds = ["workshop", "mod", ]
    assetcmd = ["missing critical assets", "missing vehicle assets", "missing assets", "assets", "asset" , "this server is using modified version of the map", "Asset"]

    if message.content.lower() in ping:
        await message.channel.send(f"Hi {message.author.mention}, how may I help you?")


    if str(message.channel) == "💻┃bot-cmd" or "staff-cmds":
        if message.content.lower() == prefix+"usercount":
            await message.channel.send("Members: "+str(id.member_count))


    if str(message.channel) == "❓┃community-support" or "staff-cmds":

        if os.path.exists("/home/sami/Desktop/vsc/discord/mod.txt") == False:
            if message.content.lower() in modcmds:
                await message.channel.send(f"{message.author.mention} https://steamcommunity.com/sharedfiles/filedetails/?id=2669939420")
                file = open("mod.txt", "w")
                file.write("mod")
                file.close()            

        if os.path.exists("/home/sami/Desktop/vsc/discord/mod.txt") == True:
            os.system("rm /home/sami/Desktop/vsc/discord/mod.txt")


    if str(message.channel) == "❓┃community-support" or "staff-cmds":

        if os.path.exists("/home/sami/Desktop/vsc/discord/map.txt") == False:
            if "map" in message.content.lower():
                await message.channel.send(f"{message.author.mention} https://steamcommunity.com/sharedfiles/filedetails/?id=2653670482")
                file = open("map.txt", "w")
                file.write("map")       
                file.close()            

        if os.path.exists("/home/sami/Desktop/vsc/discord/map.txt") == True:
            os.system("rm /home/sami/Desktop/vsc/discord/map.txt")


    #var

    if str(message.channel) == "❓┃community-support" or "staff-cmds":
        if os.path.exists(path+cmd) == False:
            if cmd in message.content.lower():
                await message.channel.send(answer)
                file = open(cmd, "w")
                file.write(cmd)
                file.close()            

        if os.path.exists(path+cmd) == True:
            os.system("rm "+path+cmd)


    if str(message.channel) == "❓┃community-support" or "staff-cmds":
        if os.path.exists(path+cmd2) == False:
            if message.content.lower() in assetcmd:
                await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
                file = open(cmd2, "w")
                file.write("f")
                file.close()            

        if os.path.exists(path+cmd2) == True:
            os.system("rm "+path+cmd2)
    

client.run("no")