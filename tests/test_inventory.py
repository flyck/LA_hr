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
    mocker.patch("spwd.getspnam", return_value=mocker.Mock(sp_pwdp=user["password"]))
    mocker.patch("pwd.getpwall", return_value=[
        mocker.Mock(pw_name=user["name"], pw_uid=1000)
    ])
    mocker.patch("grp.getgrall", return_value=[
        mocker.Mock(gr_name=group, gr_mem=user["name"]) for group in user["groups"]
    ])
    mocker.patch("json.dumps")

    inventory.export(inventory_file)

    # groups is a list, so before we can compare it we need to sort it
    user["groups"].sort()

    json.dumps.assert_called_with([user], inventory_file, indent=4)