# Discord Music Bot

A Discord bot that plays music in voice channels using Python and Discord.py.

## Features

- Plays music from YouTube URLs in voice channels.
- Supports commands to play, pause, resume, and stop music playback.
- Queue functionality to manage multiple song requests.
- Announces the currently playing song and queued songs.
- Uses `yt-dlp` for extracting YouTube video URLs.

## Prerequisites

- Python 3.6 or higher
- `discord.py` library (`pip install discord.py`)
- `yt-dlp` library (`pip install yt-dlp`)
- FFmpeg installed and added to PATH

## Installation

1. Clone the repository:

   git clone https://github.com/YourUsername/discord-music-bot.git
   cd discord-music-bot

2. Install dependencies:

    pip install -r requirements.txt

3. Set up environment variables:

    Create a .env file in the root directory.

    Add your Discord bot token to the .env file:
        DISCORD_TOKEN=your_discord_bot_token

    Note: Ensure .env is added to your .gitignore file to keep your token secret.

4. Run the bot:

    python main.py

## Usage

- Join a voice channel in your Discord server.
- Use the following commands prefixed with `dreamy` (or modify as needed):

  - `dreamyplay <YouTube URL>`: Plays music from the provided YouTube URL.
  - `dreamypause`: Pauses the currently playing music.
  - `dreamyresume`: Resumes paused music playback.
  - `dreamystop`: Stops playing music and disconnects the bot from the voice channel.
  - `dreamyskip`: Skips the currently playing song and plays the next song in the queue.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

### Notes:

- Replace `YourUsername` with your actual GitHub username in the repository URL.
- Replace `your_discord_bot_token` with your actual Discord bot token in the `.env` setup section.
- Ensure you have Python, necessary libraries (`discord.py`, `yt-dlp`), and FFmpeg installed before running the bot.
- Customize commands (`dreamyplay`, `dreamypause`, etc.) to fit your bot's prefix or naming convention.

### Features to implement in the future

1. Repeat Functionality - able to repeat certain tracks 
2. Playlist Support - able to play whole playlists
3. randomize queue or playlist given - randomize current queue or tracks
4. Song Search - able to just type the title of the song or other details then play music the one the program searches
5. Now Playing Command - enhance the currently playing command, currently it only display title. in the future i will try to add the duration.
6. Error Handling and Logging: Improve error handling and log messages to help diagnose issues.
7. Music Queue Management: Enhance queue management with commands to view, reorder, remove specific songs, or clear the entire queue.
8. Shuffle Command: Allow users to shuffle the queue or playlist.
9. Integration with Music APIs: Explore integrating with music APIs like Spotify, SoundCloud, or others for broader music selection.
10. User Permissions: Implement permission checks to restrict certain commands to server admins or specific roles.
11. Cross-Server Support: Ensure the bot can handle requests and queues independently across multiple servers. (Not Sure if fixed)
12. Interactive Help Command: Create a detailed help command to guide users on how to use different features.
13. Customizable Prefix: Allow server admins to customize the bot's command prefix.
14. Pause on Disconnect: Automatically pause playback when the bot is disconnected from a voice channel due to network issues or server restarts. (not necessarily needed)
15. Vote Skip: Implement a voting system to skip songs democratically. (have voting system?)
16. Playback Statistics: Track and display statistics such as total songs played, most played songs, etc.