import subprocess

def delete(user):
    if user == "root":
        return

    try:
        return subprocess.run(["userdel", user], stdout = subprocess.PIPE)
    except:
        pass