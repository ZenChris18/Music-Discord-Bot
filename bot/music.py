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
    
    # Initialize voice_client variable
    voice_client = None

    yt_dl_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg_options = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn -filter:a "volume=0.25"'
    }

    @client.event
    async def on_ready():
        print(f"{client.user} is now online and ready to play music!")

    @client.event
    async def on_message(message):
        nonlocal voice_client

        if message.author == client.user:
            return

        if message.content.startswith("dreamyplay"):
            try:
                if message.author.voice:
                    voice_channel = message.author.voice.channel
                    voice_client = await voice_channel.connect()
                else:
                    await message.channel.send("You need to be in a voice channel to use this command.")

            except Exception as e:
                print(f"Error connecting to voice channel: {e}")

            try:
                url = message.content.split()[1]

                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

                song = data["url"]
                player = discord.FFmpegOpusAudio(song, **ffmpeg_options)

                voice_client.play(player)

            except Exception as e:
                print(f"Error playing audio: {e}")

        if message.content.startswith("dreamypause"):
            try:
                if voice_client and voice_client.is_playing():
                    voice_client.pause()
                else:
                    await message.channel.send("Nothing is playing to pause.")
            except Exception as e:
                print(f"Error pausing audio: {e}")

        if message.content.startswith("dreamyresume"):
            try:
                if voice_client and voice_client.is_paused():
                    voice_client.resume()
                else:
                    await message.channel.send("Nothing is paused to resume.")
            except Exception as e:
                print(f"Error resuming audio: {e}")

        if message.content.startswith("dreamystop"):
            try:
                if voice_client:
                    voice_client.stop()
                    await voice_client.disconnect()
                    voice_client = None  # Reset voice_client after disconnecting
                else:
                    await message.channel.send("Nothing is playing to stop.")
            except Exception as e:
                print(f"Error stopping audio: {e}")

    client.run(TOKEN)

