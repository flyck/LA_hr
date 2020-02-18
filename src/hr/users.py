import subprocess
import pwd, spwd

def delete(user):
    if user == "root":
        return

    try:
        subprocess.run(["userdel", user], stdout = subprocess.PIPE)
    except:
        pass

def create(user, groups, password):
    try:
        pwd.getpwnam(user)
    except KeyError:
        subprocess.run(
            ["useradd", user, "-G", ",".join(groups), "-p", password], 
            stdout = subprocess.PIPE
    )

def update(user, groups, password):
    """
    Update an existing user if necessary
    """
    usermod_params = []
    
    proc = subprocess.run(["groups", user], stdout = subprocess.PIPE)
    if proc != f"{user} : {' '.join(groups)}":
        print(f"Groups need an update! {proc} -> {' '.join(groups)}")
        usermod_params += ["-G", ",".join(groups)]

    spwd_info = spwd.getspnam(user)
    if spwd_info.sp_pwdp != password:
        print(f"Password needs an update! {spwd_info.sp_pwdp}")
        usermod_params += ["-p", password]

    subprocess.run(["usermod", user] + usermod_params, stdout = subprocess.PIPE)
    
