import os

def get_file_size(file):
    return os.stat(file).st_size
