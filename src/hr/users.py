import subprocess

def delete(user):
    if user == "root":
        return

    try:
        subprocess.run(["userdel", user], stdout = subprocess.PIPE)
    except:
        pass