import os, os.path
import json

def save_file(mid, sets):  
# simple version for working with CWD
    DIR = "./results"
    index = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    mid.save(f'results/track_{index}.mid')

    with open('./results/sets.txt', 'a+') as f:
        f.write(f"{index}: {json.dumps(sets)}\n")