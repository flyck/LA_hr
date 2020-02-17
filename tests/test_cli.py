import pytest

path="tests/testfile.json"

from hr import cli

def test_failure_on_no_arguments():
    """
    The cli raises an error if no arguments are given.
    """
    parser = cli.create_parser()
    with pytest.raises(SystemError):
        parser.parse([])

def test_success_if_path_is_included():
    """
    The cli raises no error if a path is given as an argument.
    """
    parser = cli.create_parser()
    assert parser.parse([path])

def test_export_true_if_flag_set():
    """
    The cli correctly sets the export flag if the export flag is set.
    """
    parser = cli.create_parser()
    args = parser.parse(["--export", path])
    assert args.export