import json
import imaplib
import email
import re
import time
from instagrapi import Client
from instagrapi.mixins.challenge import ChallengeChoice
from instagrapi.exceptions import BadPassword, TwoFactorRequired, ChallengeRequired, ChallengeUnknownStep, UnknownError

try:
    # Remove_Authorization_Data
    exec(open(f"{ModulesPath}/Remove_Authorization_Data.py").read())
    
    # Load device settings from a file
    exec(open(f"{ModulesPath}/load_device_settings.py").read())
    
    # Load Password from File
    with open(f'{PasswordsPath}/{project}.txt', 'r') as file:
        password = file.read().strip()
    
    # Login Instagram
    print(f"[Trying To Relogin Account: {project}]")
    cl.login(username=project, password=password)
    
    # Save device settings to a file
    cl.dump_settings(f'{DevicesPath}/{project}.json')
    
    # Save username to file
    with open(f'{CustomersPath}/LoggedIn.txt', 'a') as f:
        f.write(project + '\n')
    
    # Remove LoggedIn Accounts from BadPassword, TwoFactorRequired, ChallengeRequired, ChallengeUnknownStep
    exec(open(f"{ModulesPath}/RemoveLoggedIn.py").read())
    
    # Print Login Status
    print(f"Account is Logged In Successfully: {project}")
    print("Please Don't Change Password... \nIf You Change Password Send Us Immediately")
except BadPassword:
    # Handle BadPassword Exception
    exec(open(f"{ModulesPath}/BadPassword.py").read())
except TwoFactorRequired:
    # Handle TwoFactorRequired Exception
    exec(open(f"{ModulesPath}/TwoFactorRequired.py").read())
except ChallengeRequired:
    # Handle ChallengeRequired Exception
    exec(open(f"{ModulesPath}/ChallengeRequired.py").read())
except ChallengeUnknownStep:
    # Handle ChallengeUnknownStep Exception
    exec(open(f"{ModulesPath}/ChallengeUnknownStep.py").read())
except UnknownError as e:
    # Handle UnknownError Exception
    print(f"Failed to Relogin: {e}")
    exec(open(f"{ModulesPath}/UnknownError.py").read())
except Exception as e:
    print(f"Failed to Relogin: {e}")

