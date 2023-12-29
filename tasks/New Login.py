import time
import os
import fileinput
import os
import csv
import json
import time
import random
import subprocess
import configparser
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagrapi.exceptions import BadPassword
from instagrapi.exceptions import TwoFactorRequired
from instagrapi.exceptions import ChallengeRequired
from instagrapi.exceptions import ChallengeUnknownStep
from instagrapi.exceptions import LoginRequired
from urllib3.exceptions import MaxRetryError
from datetime import datetime

# Create a Client Object
cl = Client()

# DatabasePaths in config.ini
config = configparser.ConfigParser()
config.read(f'C:/Program Files/BAD/blackaquapython/tasks/Config.BlackAqua.ini')
CachePath = config.get('DatabasePaths', 'CachePath')
CommentsPath = config.get('DatabasePaths', 'CommentsPath')
CustomersPath = config.get('DatabasePaths', 'CustomersPath')
DevicesPath = config.get('DatabasePaths', 'DevicesPath')
EmailsPath = config.get('DatabasePaths', 'EmailsPath')
PasswordsPath = config.get('DatabasePaths', 'PasswordsPath')
StoriesPath = config.get('DatabasePaths', 'StoriesPath')
# PythonPaths in config.ini
PythonPath = config.get('PythonPaths', 'PythonPath')
ModulesPath = config.get('PythonPaths', 'ModulesPath')


folder_path = "C:/BlackAquaPython/devices/"
output_file = "C:/BlackAquaPython/customers/All.txt"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Open the output file for writing
with open(output_file, "w") as file:
    # Iterate through the list of files and extract only the file names
    for f in files:
        if os.path.isfile(os.path.join(folder_path, f)):
            file.write(f + "\n")  # write each file name on a new line


# Open the file in read mode
with fileinput.FileInput(output_file, inplace=True) as file:
    # Iterate through each line in the file
    for line in file:
        # Replace ".json" with "NO TEXT" and print the modified line
        print(line.replace('.json', ''), end='')

# Get the current date and time
current_datetime = datetime.now()
# Format the date and time
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_datetime)

# Prompt user to enter a username
project = input("Please enter your username: ").strip()

# Prompt user to enter a password
password = input("Please enter your password (leave blank if none): ").strip()

# Save username to a file
with open("C:/BlackAquaPython/customers/ReLogin.txt", "w") as f:
    f.write(project)
    print("Username saved to file.")

# Save password to a file if not empty
if password != "":
    with open(f"C:/BlackAquaPython/passwords/{project}.txt", "w") as f:
        f.write(password)
        print("Password saved to file.")

# Check if username is in specific file, execute specific code if not found
with open("C:/BlackAquaPython/customers/All.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

if project in lines:
    # Do something if the username is found in the file
    print(f"Username already registered: {project}")
    time.sleep(1)
    exec(open(f"C:/BlackAquaPython/python/modules/Login_New.py").read())
    time.sleep(1)
    exec(open(f"C:/BlackAquaPython/python/modules/official_accounts.py").read())
    time.sleep(3)
else:
    # Do something else if the username is not found in the file
    print(f"Username not registered: {project}")
    print(f"Creating Device: {project}")
    time.sleep(1)
    try:
        with open(f"C:/BlackAquaPython/comments/customers.txt", 'r', encoding='utf-8') as file:
            comments = file.read()
        with open(f"C:/BlackAquaPython/comments/{project}.txt", 'w', encoding='utf-8') as file:
            file.write(comments)
            time.sleep(3)
    except Exception as e:
        print(f"Failed to Create Comments: {e}")
    exec(open(f"C:/BlackAquaPython/python/modules/Create_Device.py").read())
    time.sleep(1)
    exec(open(f"C:/BlackAquaPython/python/modules/Login_New.py").read())
    time.sleep(1)
    exec(open(f"C:/BlackAquaPython/python/modules/official_accounts.py").read())
    time.sleep(1)

