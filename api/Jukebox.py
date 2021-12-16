import os, subprocess

master = os.openpty()
slave = master

class Jukebox:
    def __init__(self):
        if not os.path.isdir("songs"):
            os.mkdir("songs")

        self.q = []
        self.current = None

    def add(self, song):
        self.dl(song)
        self.q.append(song)

    def dl(self, song):
        subprocess.run([
            "yt-dlp", "-x", "--audio-format", "mp3", "\"ytsearch:"+song+"\"", "-o", "songs/"])

    def play(self):
        global master
        global slave

        if len(self.q) != 0:
            song = self.q.pop()
            self.current = subprocess.Popen([
                "mpg123", "-C", song], stdin=master)


    def autoplay(self):
        while True:
            if len(self.q) != 0:
                self.play()

        
