import discord
import os
client = discord.Client()
prefix = "a!"
version = "1.0.0"
author = "ADX#5452"
mapversion = "1.0.0"


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
    id = client.get_guild(870007912452468746)
    mapcmd = ["map", "workshop"]
    ping = ["@ADX", "<@917078593429987389>", "@917078593429987389", "<@ADX>"]
    modcmds = ["workshop", "mod", ]
    assetcmd = ["missing critical assets", "missing vehicle assets", "missing assets", "assets", "asset" , "this server is using modified version of the map", "Asset"]

    if message.content.lower() in ping:
        await message.channel.send(f"Hi {message.author.mention}, how may I help you?")


    if str(message.channel) == "💻┃bot-cmd" or "staff-cmds":
        if message.content.lower() == prefix+"usercount":
            #await message.channel.send("Members: "+str(id.member_count))
            embed = discord.Embed(title="Members", description=f"{id.member_count}")
            await message.channel.send(content=None, embed=embed)


    if str(message.channel) == "❓┃community-support" or "staff-cmds":
        if os.path.exists(path+"mod") == False:
            if message.content.lower() in modcmds:
                #await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
                embed = discord.Embed(title="Ice Network's Workshop Collection", description="Find all mods used by ICE RP")
                embed.add_field(name="Workshop", value="https://steamcommunity.com/sharedfiles/filedetails/?id=2669939420")
                await message.channel.send(content=None, embed=embed)
                file = open("mod", "w")
                file.write("f")
                file.close()            

        if os.path.exists(path+"mod") == True:
            os.system("rm "+path+"mod")



    if str(message.channel) == "❓┃community-support" or "staff-cmds":
        if os.path.exists(path+"map") == False:
            if message.content.lower() in mapcmd:
                #await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
                embed = discord.Embed(title="Ice Network's RP Map", description="Version: 1.0.0")
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
            if cmd in message.content.lower():
                #await message.channel.send(answer)
                embed = discord.Embed()
                embed.add_field(name="Version", value=version)
                embed.add_field(name="Author", value=author)
                embed.add_field(name="Prefix", value=prefix)
                await message.channel.send(content=None, embed=embed)
                file = open(cmd, "w")
                file.write(cmd)
                file.close()            

        if os.path.exists(path+cmd) == True:
            os.system("rm "+path+cmd)


    if str(message.channel) == "❓┃community-support" or "staff-cmds":
        if os.path.exists(path+cmd2) == False:
            if message.content.lower() in assetcmd:
                #await message.channel.send(f"{message.author.mention} Try: Remove all files from /steamapps/workshop/content/304930, Subscribe to our mods and map")
                embed = discord.Embed(title="Solutions for your problem", description="Missing Assets")
                embed.add_field(name="Subscribe to our workshop content here", value="https://steamcommunity.com/sharedfiles/filedetails/?id=2669939420")
                embed.add_field(name="Remove all workshop mods in folder", value="/steamapps/workshop/content/304930")
                await message.channel.send(content=None, embed=embed)
                file = open(cmd2, "w")
                file.write("f")
                file.close()            

        if os.path.exists(path+cmd2) == True:
            os.system("rm "+path+cmd2)
    

client.run("OTE3MDc4NTkzNDI5OTg3Mzg5.Yazd_w.GvcWLMLnwUcHAgwSFXpAOuAnbFo")