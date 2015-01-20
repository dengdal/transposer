#!/usr/bin/python

# Chord transposer program in Python
# Only handles major keyes yet, and no fault handling at all.
# David Engdal, 2015-01-18

#imports:
from string import lower
from test import testprinter

testprinter()
print "Chord transposer program in Python \n"
# init
printString = ''
fromSong = []
toSong = []
toSharpOrFlatFlag = 'null'
majorKeysSharp=['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#','b']
majorKeysFlat=['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb','b']
#minorKeysSharp=['am', 'em', 'bm', 'f#m', 'c#m', 'g#m', 'd#m', 'g', 'g#', 'a', 'a#','b']
keyError='No such key in Western music. Exiting'
chordError='No such chord in Western music. Exiting'
# input
fromKey = raw_input('From what key do you want to transpose?').lower()
toKey = raw_input('To what key do you want to transpose?').lower()
fromSongInput = raw_input('Please enter your chords to transpose separated by space:').split()

# make lower case letters of song:
for chord in fromSongInput:
    fromSong.append(chord.lower())

# Get number of steps to transpose:
if fromKey in majorKeysSharp:
    fromIx =  majorKeysSharp.index(fromKey)
elif fromKey in majorKeysFlat:
    fromIx =  majorKeysFlat.index(fromKey)
else:
    raise ValueError(keyError)
if toKey in majorKeysSharp:
    toSharpOrFlatFlag = 'Sharp'
    toIx =  majorKeysSharp.index(toKey)
elif toKey in majorKeysFlat:
    toSharpOrFlatFlag = 'Flat'
    toIx = majorKeysFlat.index(toKey)
else:
    raise ValueError(keyError)
transposeHalfSteps = (toIx - fromIx)
if transposeHalfSteps > len(majorKeysSharp)/2:
    transposeHalfSteps -= len(majorKeysSharp)
transMessage = 'You are transposing ' + repr(transposeHalfSteps) + ' half steps.' 
print transMessage

# transpose:
for chord in fromSong:
    # pick first one or two letters for transpose the first:
    if len(chord) >= 2:
        if chord[1] in ['#', 'b']: 
            rootChord=chord[:2]
            coloring=chord[2:]
        else:
            rootChord=chord[:1]
            coloring=chord[1:]
    else:
        rootChord=chord[:1]
        coloring=chord[1:]
    # check for and transpose rootChord
    if rootChord in majorKeysSharp:
        transposedRootChord =  majorKeysSharp[(majorKeysSharp.index(rootChord) + transposeHalfSteps) % len(majorKeysSharp)]
        transposedChord = transposedRootChord + coloring
    elif rootChord in majorKeysFlat:
        transposedRootChord =  majorKeysFlat[(majorKeysFlat.index(rootChord) + transposeHalfSteps) % len(majorKeysFlat)]
        transposedChord = transposedRootChord + coloring
    else:
        print 'Unknown chord in song: ' + rootChord
        raise ValueError(keyError)
    toSong.append(transposedChord)

# print toSong
for toChordIx, toChord in enumerate(toSong):
    printString += toChord + '\t'
    if (toChordIx % 8) == 7:
        print printString
        printString = ''
print printString # flush print buffer
    
