from gtts import gTTS
from time import sleep
import os
import pyglet
import tempfile
import pygame as pg
import random

def play_mp3File(mp3File, volume=0.9, freq = 24000):
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
        pg.mixer.music.load(mp3File)
        print("Music file {} loaded!".format(mp3File))
    except pg.error:
        print("File {} not found! ({})".format(mp3File, pg.get_error()))
        return
		
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

    pg.mixer.music.stop()
    pg.mixer.stop()
    pg.mixer.quit()

def do_wordtest(word):
	print(word)
	wordList.remove(word)
	fn = 'c:\\temp\\wordtest\\' + word + '.mp3'

	if os.path.isfile(fn) is True:
		print('Skip get gTTS')		
	else:
		ttsResult = gTTS(text=word, lang='en')
		fp = ttsResult.save(fn)
	play_mp3File(fn)
	sleep(3)
	play_mp3File(fn, freq = 21500)
	os.system("Pause")
    
if __name__ == "__main__":
	#wordList = ['absolutely', 'assist',  'brave', 'carry', 'choose', 'contest', 'descendant', 'distort', 'fall', 'fit' , 'hard-working', 'hope', 'investigate', 'lake', 'limit', 'manager', 'mighty', 'number', ' overseas', 'politics', 'relief', 'robber', 'scan', 'sew', 'steal', 'suitcase', 'tear', 'tiptoe', 'truth', 'yawn']
	#wordList = ['tear']
	wordList = ['account', 'ambassador', 'atomosphere', 'belong', 'brick', 'civil', 'common', 'convenient', 'custom', 'dessert', 'fantastic', 'flat', 'frozen', 'hostile', 'incident', 'last', 'million', 'package','permit','pop','professional', 'rare', 'remember','shape','stick','sunset','tomb','turtle', 'valuable', 'welcome']
	print(wordList)

	#for word in wordList:
	while len(wordList) > 0 :
		word = random.choice(wordList)
		do_wordtest(word)

	
