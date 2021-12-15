import subprocess

def addSongToQueue(songLink):
    subprocess.Popen(["ytp-dlp", "-dx", "\"ba\"", "--audio-format", "mp3", songLink])
