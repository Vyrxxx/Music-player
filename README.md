# Music Player

An open-source, local-first music player that doesn't spy on you.

No accounts required, no telemetry, no listening data harvested and sold to advertisers or "big corporations" for profit. Your playlists and songs stay on your machine. This is a hobby project built to learn Python — it's rough around the edges and actively evolving, but the philosophy is simple: **it should just play your music, not watch you do it.**

## Features

- **Play local audio files** — load and play songs straight from your computer
- **Download from YouTube** — grab audio from a YouTube URL and add it to your library
- **Automatic format conversion** — downloads are converted to `.ogg` for reliable playback and seeking
- **Playlists** — build, save, and reload playlists from a simple local playlist file
- **Playback controls** — play, pause, resume, and loop songs
- **No accounts, no tracking, no ads** — everything runs locally on your machine

## Why this exists

Most mainstream music apps come with a tradeoff most people never really agreed to: in exchange for convenience, they collect detailed listening habits, build behavioral profiles, and monetize that data — often well beyond what's needed to just play a song. This project is built the other way around. It's meant to prove that a music player doesn't need any of that to work well.

## Status

This is an early-stage, actively developed hobby project — expect rough edges, missing features, and breaking changes while it's being built out. It'll keep receiving updates until it's solid enough for everyday use.

## Installation

Requires Python 3 and [ffmpeg](https://www.gyan.dev/ffmpeg/builds/) installed and available on your system PATH (needed for audio conversion).

Install the required Python packages:

```bash
py -m pip install pytubefix pygame-ce easygui pydub customtkinter
```

## Usage

Run the player from your terminal:

```bash
py Musicplayer.py
```

Follow the on-screen menu to import a playlist, play local songs, download from YouTube, build a playlist, or play through your playlist.

## Roadmap

- [ ] Graphical interface (in progress, built with `customtkinter`)
- [ ] Skip / seek within a song
- [ ] Shareable playlists (auto re-download missing songs from saved YouTube links)
- [ ] Optional accounts for cross-device sync — no data collection, no third-party trackers

## Contributing

This is a first real project and a learning process, so the code is still maturing — issues, suggestions, and pull requests are welcome.

## License

Licensed under the [GNU General Public License v3.0](LICENSE). This keeps the project — and anything built on top of it — free and open, and protects it against being closed off or weaponized with patents down the line.
