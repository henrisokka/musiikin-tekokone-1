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
        patterns.append(create_pattern(base + n, set, False))
    print(patterns)
    return patterns

def downward_patterns(set):
    patterns = []
    for n in set:
        patterns.append(create_pattern(base - n, set, False))
    
    return patterns


if __name__ == "__main__":

    base = 64
    sets = [[0, 7, 4], [0, 7, 4, 5], [7, 4, 5], [7, 4, 5, 2], [4, 5, 2], [4, 5, 2, 9]]

    create_tracks(len(sets) * 3)

    index = 0
    for set in sets:
        add_patterns(permutation_patterns(set), index)
        add_patterns(basic_patterns(set), index + 1)
        add_patterns(downward_patterns(set), index + 2)
        index += 3

    save_file(mid)



