from moviepy.editor import *

audioclip = AudioFileClip('videoplayback.mp4')
audioclip.write_audiofile('audio.mp3', buffersize = 50000)
