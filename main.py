from mido import Message, MidiFile, MidiTrack
import random
import os, os.path

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


def new_note(note, length):
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=127, time=120 * length))


def create_pattern(base, set):
    pattern = []
    for n in set:
        up = bool(random.getrandbits(1))
        if up: note = base + n
        else: note = base - n
        pattern.append(note)
    
    return pattern

def add_to_track(pattern):
    for note in pattern:
        new_note(note, 1)

def save_file(mid):    
# simple version for working with CWD
    DIR = "./results"
    index = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    mid.save(f'results/track_{index}.mid')


base = 64
set = [0, 2, 7, 9, 11]

for n in set:
    pattern = create_pattern(base - n, set)
    print(pattern)
    add_to_track(pattern)

save_file(mid)



