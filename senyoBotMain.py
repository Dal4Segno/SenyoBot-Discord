import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()
targetChannels = {}

@bot.event
async def on_ready():
    guild_count = 0
    
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

        for channel in guild.channels:
            print(f"-- {channel}")
            if channel.type == discord.ChannelType.text and channel.name == "general":
                targetChannels[guild.id] = channel.id
    
    for k, v in targetChannels.items():
        print(f"{k} , {v}")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.self_stream == False and after.self_stream == True:
        targetChannel = bot.get_channel(targetChannels[bot.get_guild(member.guild.id).id])
        await targetChannel.send(f"**{member.name}**님이 **{after.channel.name}**에서 방송을 시작했습니다.")

    if before.self_stream == True and after.self_stream == False:
        targetChannel = bot.get_channel(targetChannels[bot.get_guild(member.guild.id).id])
        await targetChannel.send(f"**{member.name}**님이 **{after.channel.name}**에서 방송을 종료했습니다.")


bot.run(TOKEN)