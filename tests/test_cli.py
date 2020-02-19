import pytest

path="tests/testfile.json"

from hr import cli


@pytest.fixture
def parser():
    return cli.create_parser()

def test_failure_on_no_arguments(parser):
    """
    The cli raises an error if no arguments are given.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_export_true_if_flag_set(parser):
    """
    The cli correctly sets the export flag if the export flag is set.
    """
    args = parser.parse_args(["--export", path])
    assert args.export