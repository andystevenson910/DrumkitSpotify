# Drumkit Spotify Controller

Transform your USB drumkit into a Spotify controller with physical drum pads! This program maps drum pad hits to Spotify playback controls, volume adjustments, and track/playlist shortcuts for linux devices.

## Features

- Play/pause, skip, rewind, and volume control

- Quick-access buttons for favorite tracks/playlists

- "Shift" like mode using the orange pedal for additional inputs

- Easy setup

- System volume control via PulseAudio

## Requirements

- Linux system with PulseAudio

- Python 3

- `python-evdev` library

- `spt` (Spotify TUI) CLI tool

- `pactl` (PulseAudio control)

- USB drumkit (tested with Wii Rock Band drumkit)

## Installation

1. Install required packages:

```bash 
sudo apt install python3-pip pulseaudio-utils

pip3 install evdev

```

2. Install Spotify TUI:

```bash
# Follow installation instructions at:

# https://github.com/Rigellute/spotify-tui

```

3. Clone this repository:

```bash
git clone https://github.com/andystevenson910/DrumkitSpotify.git

cd DrumkitSpotify
```


## Usage
1. launch spotify

2. Run the controller:
```bash
python3 drum_controller.py

```

3. Follow on-screen prompts:

- Unplug drumkit and press Enter

- Plug in drumkit and press Enter

4. Start drumming! (See control mapping below)

## Control Mapping

### Regular Mode
Drum Pad | Function
--- | ---
Green | Next Track
Blue | Play/Pause
Yellow | Previous Track
Red | Mute/Unmute
Kick Pedal | *Modifier for colored pads*
Plus | Volume Up (+5%)
Minus | Volume Down (-5%)
Pad 1 | Play "Self Care" track
Pad 2 | Play "The Way I Am" track
Pad A | Play "Sabotage" track
Pad B | Play "Island in the Sun"

### Orange Button Mode (Hold Orange + Hit Pad)
Drum Pad | Function
--- | ---
Green | Volume Up (+10%)
Red | Volume Down (-10%)
Yellow | Play Top 2022 Playlist
Blue | Play Top 10 Playlist
Plus | Max Volume (100%)
Minus | Low Volume (10%)
## Troubleshooting

- **Device not detected**:

Run `ls /dev/input` to verify drumkit appears as `event*`


- **Spotify commands fail**:

Verify `spt` is authenticated and Spotify client is running

## Customization

Edit these sections to customize:

- Tracks/playlists: Search for `os.system("spt play --uri` and replace URIs
