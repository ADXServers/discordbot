import discord
import os
client = discord.Client()
prefix = "a!"
version = "1.0.0"
author = "ADX#5452"

path = "/home/sami/Desktop/vsc/discord/"
path = "/home/sami/Desktop/vsc/discord/"


cmd = "info"
answer = "Author: "+author+"\nVersion: "+version+"\nPrefix: "+prefix

cmd2 = "asset"

@client.event
async def on_message(message):
    global said
    id = client.get_guild(870007912452468746)
    if message.content == prefix+"usercount":
        await message.channel.send("Members: "+str(id.member_count))

    if os.path.exists("/home/sami/Desktop/vsc/discord/mod.txt") == False:
        if "mod" in message.content:
            await message.channel.send(f"{message.author.mention} https://steamcommunity.com/sharedfiles/filedetails/?id=2669939420")
            file = open("mod.txt", "w")
            file.write("mod")
            file.close()            

    if os.path.exists("/home/sami/Desktop/vsc/discord/mod.txt") == True:
        os.system("rm /home/sami/Desktop/vsc/discord/mod.txt")



    if os.path.exists("/home/sami/Desktop/vsc/discord/map.txt") == False:
        if "map" in message.content:
            await message.channel.send(f"{message.author.mention} https://steamcommunity.com/sharedfiles/filedetails/?id=2653670482")
            file = open("map.txt", "w")
            file.write("map")       
            file.close()            

    if os.path.exists("/home/sami/Desktop/vsc/discord/map.txt") == True:
        os.system("rm /home/sami/Desktop/vsc/discord/map.txt")


    #var

    if os.path.exists(path+cmd) == False:
        if cmd in message.content:
            await message.channel.send(answer)
            file = open(cmd, "w")
            file.write(cmd)
            file.close()            

    if os.path.exists(path+cmd) == True:
        os.system("rm "+path+cmd)



    if os.path.exists(path+cmd2) == False:
        if cmd2 in message.content:
            await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
            file = open(cmd2, "w")
            file.write("f")
            file.close()            

    if os.path.exists(path+cmd2) == True:
        os.system("rm "+path+cmd2)
    

client.run("OTE3MDc4NTkzNDI5OTg3Mzg5.Yazd_w.ofjTnFhHg8UfJOiW000Ifv2MAdA")