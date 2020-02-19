import json

import spwd, pwd, grp

def read(path):
    """
    Read the inventory from a given json file.
    """
    with open(path) as f:
        inventory = json.load(f)

    return inventory

def export(path):
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

        my_inventory.append({
            "name": user,
            "groups": groups,
            "password": password
        })

    json.dumps(my_inventory, path, indent=4)
        
