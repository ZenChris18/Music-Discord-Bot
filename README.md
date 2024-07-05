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

