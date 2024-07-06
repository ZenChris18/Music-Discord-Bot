import discord
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    TOKEN = os.getenv("discord_token")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    # Dictionary to store voice_client instances and queues for each server
    voice_clients = {}
    queues = {}

    yt_dl_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg_options = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn -filter:a "volume=0.25"'
    }

    @client.event
    async def on_ready():
        print(f"{client.user} is now online and ready to play music!")
        await self_ping()

    async def self_ping():
        await asyncio.sleep(60)  # Sleep for 600 seconds (10 minutes)
        await client.wait_until_ready()
        print("Self ping executed.")  # Log a message indicating self ping execution
        await self_ping()  # Schedule the next self ping

    async def play_next(guild_id, text_channel):
        if queues[guild_id]:
            url = queues[guild_id].pop(0)
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
            
            song = data["url"]
            title = data["title"]
            player = discord.FFmpegOpusAudio(song, **ffmpeg_options)
            
            voice_clients[guild_id].play(player, after=lambda e: client.loop.create_task(play_next(guild_id, text_channel)))
            await text_channel.send(f"Now playing: {title}") # Adds text of what is now playing

    @client.event
    async def on_message(message):
        # Use guild ID to manage voice clients per server
        guild_id = message.guild.id

        if message.author == client.user:
            return

        if message.content.startswith("dreamyplay"):
            try:
                if message.author.voice:
                    voice_channel = message.author.voice.channel
                    if guild_id in voice_clients:
                        voice_client = voice_clients[guild_id]
                        if voice_client.is_connected():
                            await voice_client.move_to(voice_channel)
                        else:
                            voice_client = await voice_channel.connect()
                    else:
                        voice_client = await voice_channel.connect()
                        voice_clients[guild_id] = voice_client
                    if guild_id not in queues:
                        queues[guild_id] = []
                else:
                    await message.channel.send("You need to be in a voice channel to use this command.")
                    return

            except Exception as e:
                print(f"Error connecting to voice channel: {e}")
                return

            try:
                url = message.content.split()[1]
                queues[guild_id].append(url)
                if not voice_clients[guild_id].is_playing():
                    await play_next(guild_id, message.channel)
                else:
                    data = await asyncio.get_event_loop().run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
                    title = data["title"]
                    queue_position = len(queues[guild_id])
                    await message.channel.send(f"'{title}' added to queue. Position: {queue_position}")

            except Exception as e:
                print(f"Error adding song to queue: {e}")

        if message.content.startswith("dreamypause"):
            try:
                if guild_id in voice_clients and voice_clients[guild_id].is_playing():
                    voice_clients[guild_id].pause()
                else:
                    await message.channel.send("Nothing is playing to pause.")
            except Exception as e:
                print(f"Error pausing audio: {e}")

        if message.content.startswith("dreamyresume"):
            try:
                if guild_id in voice_clients and voice_clients[guild_id].is_paused():
                    voice_clients[guild_id].resume()
                else:
                    await message.channel.send("Nothing is paused to resume.")
            except Exception as e:
                print(f"Error resuming audio: {e}")

        if message.content.startswith("dreamystop"):
            try:
                if guild_id in voice_clients:
                    voice_clients[guild_id].stop()
                    await voice_clients[guild_id].disconnect()
                    del voice_clients[guild_id]  # Remove the voice_client from the dictionary
                    queues[guild_id].clear()  # Clear the queue for the guild
                else:
                    await message.channel.send("Nothing is playing to stop.")
            except Exception as e:
                print(f"Error stopping audio: {e}")

        if message.content.startswith("dreamyskip"):
            try:
                if guild_id in voice_clients and voice_clients[guild_id].is_playing():
                    voice_clients[guild_id].stop()
                    await play_next(guild_id, message.channel)
                else:
                    await message.channel.send("Nothing is playing to skip.")
            except Exception as e:
                print(f"Error skipping audio: {e}")

    client.run(TOKEN)

