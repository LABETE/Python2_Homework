import os
import glob

def CountFilesInDirectory():
    files = glob.glob(os.path.basename("*"))
    dict_directory_files = {}
    for file in files:
        name, ext = file.split(".")
        dict_directory_files[ext] = dict_directory_files.get(ext, 0) + 1
    return dict_directory_files