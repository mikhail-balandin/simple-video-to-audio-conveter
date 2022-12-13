from moviepy.editor import *

URL = 'https://www.youtube.com/watch?v=4w4sSabOjl0&ab_channel=PythonToday'
audioclip = AudioFileClip(URL)
audioclip.write_audiofile('audioo.mp3', buffersize = 50000)