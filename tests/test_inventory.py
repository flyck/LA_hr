import pytest
import json

import pwd, spwd, grp

from hr import inventory

inventory_file = "tests/testfile.json"

user = {
    "name": "kevin",
    "groups": ["wheel", "users"],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
}


def test_inventory_read(mocker):
    """
    The inventory is read as a json.
    """
    mocker.patch("json.load")

    my_inventory = inventory.read(inventory_file)

    json.load.assert_called()

def test_inventory_export(mocker):
    """
    The export function generates the expected output for a given user.
    """
    fake_spwd = spwd.struct_spwd(
        (user["name"], 
        user["password"], 
        18310, 0, 99999, 7, -1, -1, -1)
    )
    fake_pwds = [
        pwd.struct_passwd(
                (user["name"], 'x', 1000, 1000, '', f'/home/{user["name"]}', '/bin/sh')
        )
    ] 
    fake_grps = [
        grp.struct_group(
            ('users', 'x', 100, [user["name"]])
        ),
        grp.struct_group(
           ('wheel', 'x', 100, [user["name"]])
        )
    ]
    
    mocker.patch("spwd.getspnam", return_value=fake_spwd)
    mocker.patch("pwd.getpwall", return_value=fake_pwds)
    mocker.patch("grp.getgrall", return_value=fake_grps)
    mocker.patch("json.dumps")

    inventory.export(inventory_file)

    # groups is a list, so before we can compare it we need to sort it
    user["groups"].sort()

    json.dumps.assert_called_with([user], inventory_file, indent=4)