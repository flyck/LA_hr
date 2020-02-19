import pytest
import subprocess
import pwd, spwd
import grp

from hr import users

user = {
    "name": "kevin",
    "groups": ["wheel", "users"],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
}

def test_deletion_of_nonexistend_user(mocker):
    """
    If the user doesn"t exist, the function shouldn"t fail.
    """
    mocker.patch("subprocess.run", side_effect=OSError("no such user"))
    exception = None
    try:
        users.delete(user["name"])
    except Exception as err:
        exception = err

    assert exception == None

def test_deletion_of_existing_user(mocker):
    """
    If the user exists, the function should delete him.
    """
    mocker.patch("subprocess.run")
    users.delete(user["name"])
    subprocess.run.assert_called_with(["userdel", user["name"]], stdout = subprocess.PIPE)

def test_creation_of_nonexisting_user(mocker):
    """
    If the user doesn't exists, the function should create him.
    """
    mocker.patch("subprocess.run")
    mocker.patch("pwd.getpwnam", side_effect=KeyError)
    
    users.create(user["name"], user["groups"], user["password"])
    subprocess.run.assert_called_with(
            ["useradd", user["name"], "-G", ",".join(user["groups"]), "-p", user["password"]], 
            stdout = subprocess.PIPE
    )
    
def test_modification_of_existing_user_update_groups(mocker):
    """
    If the user exists but the groups mismatch, the function should update those groups.
    """
    mocker.patch("spwd.getspnam", return_value=mocker.Mock(sp_pwdp=user["password"]))
    mocker.patch("grp.getgrall", return_value=[
        mocker.Mock(gr_name=group, gr_mem=[]) for group in user["groups"]
    ])
    mocker.patch("subprocess.run")
    
    users.update(user["name"], user["groups"], user["password"])

    subprocess.run.assert_called_with(
            ["usermod", user["name"], "-G", ",".join(user["groups"])], 
            stdout = subprocess.PIPE
    )

def test_modification_of_existing_user_update_password(mocker):
    """
    If the user exists but the password mismatches, the function should update it.
    """
    mocker.patch("spwd.getspnam", return_value=mocker.Mock(sp_pwdp="some_wrong_password"))
    mocker.patch("grp.getgrall", return_value=[
        mocker.Mock(gr_name=group, gr_mem=user["name"]) for group in user["groups"]
    ])
    mocker.patch("subprocess.run")
    
    users.update(user["name"], user["groups"], user["password"])

    subprocess.run.assert_called_with(
            ["usermod", user["name"], "-p", user["password"]], 
            stdout = subprocess.PIPE
    )

def test_no_action_if_update_not_needed(mocker):
    """
    If the user matches perfectly the function shouldn't do anything.
    """
    mocker.patch("spwd.getspnam", return_value=mocker.Mock(sp_pwdp=user["password"]))
    mocker.patch("grp.getgrall", return_value=[
        mocker.Mock(gr_name=group, gr_mem=user["name"]) for group in user["groups"]
    ])
    mocker.patch("subprocess.run", side_effect=Exception)
    
    exception = None
    try:
        users.update(user["name"], user["groups"], user["password"])
    except Exception as e:
        exception = e

    assert exception == None