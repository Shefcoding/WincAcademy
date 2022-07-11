__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import pathlib
import zipfile
import os, shutil
from os import listdir
from os.path import isfile, join

def clean_cache():

    if os.path.exists('./files/cache'):
        shutil.rmtree('./files/cache')
    os.mkdir('./files/cache')

def cache_zip(zip,cache):
    with zipfile.ZipFile(zip, 'r') as zip_ref:
        zip_ref.extractall(cache)

def cached_files():
    #files_path = [os.path.abspath(cwd) for cwd in os.listdir(cwd) if not os.path.isfile(cwd)]
    #return files_path
    all_cache_files = []
    my_cache_dir = os.path.abspath('./files/cache')
    for file in os.listdir(my_cache_dir):
        filepath = os.path.join(my_cache_dir, file)
        all_cache_files.append(filepath)
    return all_cache_files

def find_password(path):
    for file in path:
        with open(file) as file:
           data=file.readlines()
           for line in data:
            if "password" in line:
             passline = line
    password = passline.split(" ",1)
    
    return password[1][:-1]

            
find_password(cached_files())
cache_zip('C:\\Users\\Gebruiker\\Documents\\wincademy\\files\\data.zip','C:\\Users\\Gebruiker\\Documents\\wincademy\\files\\cache')
print(cached_files())
print(clean_cache())
