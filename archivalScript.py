import os
import shutil
import pathlib
from os import listdir
from os.path import isfile, join
import re
import datetime
from os import walk
from pathlib import Path


def copyReplays(old_directory, new_directory):

    #   check if the directory already exists
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)
        print(f"Directory {new_directory} Created.")
    else:    
        print(f"Directory {new_directory} already exists.")

    # check if lastSessionData exists
    if not os.path.isfile(join(new_directory + "/" + "lastSessionData")):
        print("lastSessionData not found, creating new log.")
        f = open(new_directory + "/" + "lastSessionData", "x")
        f.write(latestReplayDate)
        f.close()
    else:
        print("Previous session found.")
        original = open(new_directory + "/" + "lastSessionData", "r")
        content = original.read()
        original.close()
        if re.findall(latestReplayDate, content):
            print("There hasn't been a new session")
            quit("There hasn't been a new session since the last save. Exiting.")
        with open(new_directory + "/" + "lastSessionData", "w") as modified:
            modified.write(latestReplayDate + '\n' + content)

    os.mkdir(new_directory + '/' + latestReplayDate)

    f = []
    for (dirpath, dirnames, filenames) in walk(old_directory):
        f.extend(filenames)
        break

    for i in f:
        if re.findall("REP", i):
            shutil.copyfile(old_directory + '/' + i, new_directory + '/' + latestReplayDate + '/' + i)
            print(f"copying{i}")


old_directory = 'C:/Users/Linzi/AppData/Local/GGST/Saved/SaveGames/79218385'
new_directory = 'C:/Users/Linzi/Desktop/Gaming Saves/GGStrive'

#   get the latest replay data date
if os.path.isfile(old_directory + "/" + "REPLAY.sav"):
    latestReplayDate = datetime.datetime.fromtimestamp(Path((old_directory + "/" + "REPLAY.sav")).stat().st_mtime).strftime("%y-%m-%d")
else:
    print("No replay data found at this location")
    quit("No replay data found at this location")

copyReplays(old_directory, new_directory)
