import subprocess
import pwd, spwd

def delete(user):
    # Don't touch root!
    if user == "root":
        return

    try:
        print(f"Deleting user {user}.", end = " ")
        subprocess.run(["userdel", user], stdout = subprocess.PIPE)
        print("Done.")
    except:
        print("Failed!")

def create(user, groups, password):
    """
    Creates a user if it doesn't exist.
    """
    user_nonexistend = False
    try:
        pwd.getpwnam(user)
    except KeyError:
        user_nonexistend = True

    if user_nonexistend:
        try: 
            print(f"Creating user {user}.", end = " ")
            subprocess.run(
                ["useradd", user, "-G", ",".join(groups), "-p", password], 
                stdout = subprocess.PIPE
            )
            print("Done.")
        except:
            print("Failed!")
        return True
    else:
        return False
        

def update(user, groups, password):
    """
    Updates an existing user if necessary.
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

    if usermod_params:
        try:
            print(f"Updating user {user}.", end = " ")
            subprocess.run(["usermod", user] + usermod_params, stdout = subprocess.PIPE)
            print("Done.")
        except:
            print("Failed!")


def manage(users):
    for user in users:
        try:
            name = user["name"]
            groups = user["groups"]
            password = user ["password"]
        except KeyError:
            print(f"Error. User information incomplete. Skipping: {user}")
        else:
            create(name, groups, password)
            update(name, groups, password)