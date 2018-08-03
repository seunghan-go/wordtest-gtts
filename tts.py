from gtts import gTTS
from time import sleep
import os
import pyglet
import tempfile
import pygame as pg


def play_music(music_file, volume=0.9, freq = 24000):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    #freq = 24000     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
		
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

    pg.mixer.music.stop()
    pg.mixer.stop()
    pg.mixer.quit()

    
#wordList = ['absolutely', 'assist',  'brave', 'carry', 'choose', 'contest', 'descendant', 'distort', 'fall', 'fit' , 'hard-working', 'hope', 'investigate', 'lake', 'limit', 'manager', 'mighty', 'number', ' overseas', 'politics', 'relief', 'robber', 'scan', 'sew', 'steal', 'suitcase', 'tear', 'tiptoe', 'truth', 'yawn']
wordList = ['tear']
print(wordList)
for word in wordList:
	print(word)

	fn = 'c:\\temp\\wordtest\\' + word + '.mp3'

	if os.path.isfile(fn) is True:
		print('Skip get gTTS')		
	else:
		ttsResult = gTTS(text=word, lang='en')
		fp = ttsResult.save(fn)
	play_music(fn)
	sleep(3)
	play_music(fn, freq = 21500)
	os.system("Pause")


	
