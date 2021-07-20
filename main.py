from mido import Message, MidiFile, MidiTrack
from src.helpers import save_file

import random
import sys

mid = MidiFile()

def create_tracks(amount):
    for i in range(amount):
        track = MidiTrack()
        mid.tracks.append(track)


def new_note(track_index, note, length):
    print(f"track_index: {track_index}")
    mid.tracks[track_index].append(Message('note_on', note=note, velocity=64, time=0))
    mid.tracks[track_index].append(Message('note_off', note=note, velocity=127, time=120 * length))


def create_pattern(base, set, random_invert=True):
    pattern = []
    for n in set:
        if random_invert is False: up = True
        else: up = bool(random.getrandbits(1))

        if up: note = base + n
        else: note = base - n
        pattern.append(note)
    
    return pattern

def add_to_track(pattern, track_index=0):
    for note in pattern:
        new_note(track_index, note, 1)
    
def add_patterns(patterns, track_index=0):
    for p in patterns:
        add_to_track(p, track_index=track_index)

def permutation_patterns(set):
    patterns = []
    for i in range(len(set)):
        n = set[i]
        patterns.append(create_pattern(base + n, set[:i+1]))

    for i in range(len(set)):
        n = set[i]
        patterns.append(create_pattern(base - n, set[i:]))
    print(patterns)
    return patterns
    
def basic_patterns(set):
    patterns = []
    for n in set:
        patterns.append(create_pattern(base + n, set))
    print(patterns)
    return patterns


def modify_set(seed, history):
    next_set = seed.copy()
    to_modify = random.randrange(len(seed))

    if to_modify in history:
        return modify_set(seed, history)

    if bool(random.getrandbits(1)): modifier = 2
    else: modifier = -2

    if bool(random.getrandbits(1)):
        modifier += 1

    next_set[to_modify] += modifier

    history.append(to_modify)
    if len(history) > len(seed) / 2:
        history = history[1:]

    return next_set, history


if __name__ == "__main__":

    base = 64
    sets = [[0, 7, 9, 2, 5]]
    history = []
    for i in range(5):
        new_set, history = modify_set(sets[i], history)
        sets.append(new_set)

    create_tracks(2)

    for set in sets:
        for i in range(4):
            add_patterns(permutation_patterns(set), 0)
            add_patterns(basic_patterns(set), 1)

    save_file(mid, sets)



