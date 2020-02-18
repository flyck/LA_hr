import pytest
import subprocess

from hr import users

username = "pythontestuser"

def test_deletion_of_nonexistend_user(mocker):
    """
    If the user doesn't exist, the function shouldn't fail.
    """
    mocker.patch('subprocess.run')
    exception = None
    try:
        users.delete(username)
    except Exception as err:
        exception = err

    assert exception == None

def test_deletion_of_existing_user(mocker):
    """
    If the user exists, the function should delete him.
    """
    mocker.patch('subprocess.run')
    assert users.delete(username)
    subprocess.run.assert_called_with(['userdel', username], stdout = subprocess.PIPE)

    