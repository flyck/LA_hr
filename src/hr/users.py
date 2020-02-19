import subprocess
import pwd, spwd, grp
from copy import deepcopy

def delete(user):
    # Don't touch root!
    if user == "root":
        return

    try:
        print(f"Deleting user {user}.", end = " ")
        subprocess.run(["userdel", user], stdout = subprocess.PIPE)
        print("Done.")
    except Exception as e:
        print("Failed!")
        print(e)

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
            # remove the group which is named after the user. will be created from useradd.
            groupscopy = deepcopy(groups)
            if user in groupscopy:
                groupscopy.remove(user)

            print(f"Creating user {user}.", end = " ")
            subprocess.run(
                ["useradd", user, "-G", ",".join(groupscopy), "-p", password], 
                stdout = subprocess.PIPE
            )
            print("Done.")
        except Exception as e:
            print("Failed!")
            print(e)
        

def update(user, groups, password):
    """
    Updates an existing user if necessary.
    """
    usermod_params = []
    
    existing_groups = [x.gr_name for x in grp.getgrall() if user in x.gr_mem]
    existing_groups.sort()
    groups.sort()
    if existing_groups != groups:
        print(f"Groups need an update! {existing_groups} -> {groups}")
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
        except Exception as e:
            print("Failed!")
            print(e)


def sync(users):
    for user in users:
        try:
            name = user["name"]
            groups = user["groups"]
            password = user["password"]
        except KeyError:
            print(f"Error. User information incomplete. Skipping: {user}")
        else:
            create(name, groups, password)
            update(name, groups, password)

    existing_users = [x.pw_name for x in pwd.getpwall() if x.pw_uid >= 1000]
    for existing_user in existing_users:
        if existing_user not in [x["name"] for x in users]:
            delete(existing_user)
    