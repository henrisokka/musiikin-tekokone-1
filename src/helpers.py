import os, os.path

def save_file(mid):    
# simple version for working with CWD
    DIR = "./results"
    index = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    mid.save(f'results/track_{index}.mid')