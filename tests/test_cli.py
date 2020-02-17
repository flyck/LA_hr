import pytest

from hr import cli

def test_failure_on_no_arguments():
    """
    The cli raises an error if no arguments are given.
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse([])
