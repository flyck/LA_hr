import pytest
from random import randrange
import subprocess

from hr import users

def test_deletion_of_nonexistend_user():
    """
    If the user doesn't exist, the function shouldn't fail.
    """
    username = f"pytestuser{randrange(10000, 20000)}"
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
    username = "mypythontest" #f"pytestuser{randrange(10000, 20000)}"
    mocker.patch('subprocess.run')
    assert users.delete(username)
    subprocess.run.assert_called_with(['userdel', username], stdout = subprocess.PIPE)

    