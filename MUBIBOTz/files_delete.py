import os

def delete_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
