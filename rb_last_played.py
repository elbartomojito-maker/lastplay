"""
Rhythmbox Last Played Plugin
===========================

This plugin saves the last played track in Rhythmbox and can restore it on startup.
"""

import gi
gi.require_version('RhythmDB', '3.0')
import os
from gi.repository import RhythmDB
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Gdk

class LastPlayedPlugin:
    def __init__(self, rb):
        self.rb = rb
        self.db = rb.get_database()
        self.last_played_file = os.path.expanduser('~/.local/share/rhythmbox/last_played')

        # Load last played track on startup
        self.load_last_played()

        # Connect to the "playback-started" signal
        rb.connect('playback-started', self.on_playback_started)

    def on_playback_started(self, player, track):
        # Save the current track to the last played file
        self.save_last_played(track)

    def save_last_played(self, track):
        uri = track.get_string(RhythmDB.PROP_MTP_URI)
        with open(self.last_played_file, 'w') as f:
            f.write(uri)

    def load_last_played(self):
        if os.path.exists(self.last_played_file):
            with open(self.last_played_file, 'r') as f:
                uri = f.read().strip()
                track = self.db.lookup_by_uri(uri)
                if track:
                    self.rb.get_player().set_playing_track(track)  

def plugin_init(rb):
    return LastPlayedPlugin(rb)
