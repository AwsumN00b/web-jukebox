import os, subprocess, vlc

master = os.openpty()
slave = master

class Jukebox:
    def __init__(self):
        if not os.path.isdir("songs"):
            os.mkdir("songs")

        self.q = []
        self.vlc = vlc.Instance()
        self.current = None

    def add(self, song):
        self.dl(song)
        self.q.append(song)

    def dl(self, song):
        ytsearch = f"ytsearch:{song}"

        subprocess.run([
            "yt-dlp", "-x", "--audio-format", "mp3", ytsearch, "-o", "songs/%(title)s.%(ext)s"
            ])

    def play(self):
        global master
        global slave

        if len(self.q) != 0:
            song = self.q.pop()
            self.current = self.vlc.media_new(song)
            self.vlc.set_media(self.current)
            time.sleep(1.5)
            duration = self.vlc.get_length() / 1000
            time.sleep(duration)


    def autoplay(self):
        while True:
            if len(self.q) != 0:
                self.play()
