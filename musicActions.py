import dbus

# Set up the D-Bus session bus
session_bus = dbus.SessionBus()

# Get the Spotify service object
spotify_bus = session_bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')

# Get the Spotify interface object
spotify_iface = dbus.Interface(spotify_bus, 'org.mpris.MediaPlayer2.Player')

def play():
    spotify_iface.Play()

def pause():
    spotify_iface.Pause()

def fast_forward():
    spotify_iface.Seek(3000000000)

def rewind():
    spotify_iface.Seek(-3000000000)



