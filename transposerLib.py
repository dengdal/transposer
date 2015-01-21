#!/usr/bin/python

# Chord transposer program in Python
# Only handles major keyes yet, and no fault handling at all.
# David Engdal, 2015-01-18

#imports:
from PyQt4.QtCore import QString
from string import lower

# init
fromSong = []
toSong = []
toSharpOrFlatFlag = 'null'
majorKeysSharp=['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#','b']
majorKeysFlat=['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb','b']
#minorKeysSharp=['am', 'em', 'bm', 'f#m', 'c#m', 'g#m', 'd#m', 'g', 'g#', 'a', 'a#','b']
keyError='No such key in Western music. Exiting'
chordError='No such chord in Western music. Exiting'

# Get number of steps to transpose:
def calcNoOfSteps(fromKey,toKey):
    transposeHalfSteps = 0
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
    return transposeHalfSteps

# transpose:
def transpose(transposeHalfSteps, fromSongInput):
    fromSongInput =  str(fromSongInput).split()
    # make lower case letters of song:
    for chord in fromSongInput:
            fromSong.append(chord.lower())

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
    return toSong
