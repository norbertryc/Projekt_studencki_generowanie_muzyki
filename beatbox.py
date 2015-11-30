#!/usr/bin/env python
#coding=utf-8  

import sys
import numpy as np
import scipy.io.wavfile



print(str(sys.argv[1]))

file = open(str(sys.argv[1])+'song.txt')

lines = [line.rstrip('\n') for line in file]

print(lines)

song = [scipy.io.wavfile.read(str(sys.argv[1])+'track'+t+'.wav')[1] for t in lines]

song = np.concatenate(song)
song = np.r_[song]

print(song)

scipy.io.wavfile.write(str(sys.argv[1])[:-1]+'.wav',
                       44100,
                       np.int16(song/max(np.abs(song))*32767))


#import pyglet
#song = pyglet.media.load(str(sys.argv[1])[:-1]+'.wav')
#song.play()
#pyglet.app.run()