import json
import sys
import spwd
import pwd
import grp

def read(path):
    """
    Read the inventory from a given json file.
    """
    try:
        with open(path) as f:
            inventory = json.load(f)
        return inventory
    except Exception:
        print("Couldn't read from file. Aborting.")
        sys.exit(1)

def export(mypath):
    """
    Write the existing users to a json file.
    """
    # get all non-system users
    users = [x.pw_name for x in pwd.getpwall() if x.pw_uid >= 1000]

    my_inventory = []
    for user in users:
        groups = [group.gr_name for group in grp.getgrall() if user in group.gr_mem]
        groups.sort()

        try:
            password = spwd.getspnam(user).sp_pwdp
        except Exception:
            password = ""


        my_inventory += [{
            "name": user,
            "groups": groups,
            "password": password
        }]

    with open(mypath, 'w') as outfile:
        json.dump(my_inventory, outfile, indent=4)

    print(f"Inventory exported to {mypath}")
        
