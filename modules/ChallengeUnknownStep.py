# If login is successful, do something
print("ChallengeUnknownStep")

# If login fails due to bad password, save the username to a file
with open(f"{CustomersPath}/Locked.txt", "a") as f:
    f.write(project + '\n')

try:
    # Remove Line from LoggedIn, BadPassword, TwoFactorRequired, UnknownError
    filenames = [f"{CustomersPath}/LoggedIn.txt", f"{CustomersPath}/BadPassword.txt", f"{CustomersPath}/TwoFactorRequired.txt", f"{CustomersPath}/UnknownError.txt"]
    for filename in filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        with open(filename, 'w') as f:
            [f.write(l) for l in lines if l.strip() != project]
except Exception as e:
    print(f"")
