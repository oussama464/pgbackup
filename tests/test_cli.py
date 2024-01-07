import pytest
from pgbackup import cli


@pytest.fixture
def parser():
    return cli.create_parser()


url = "postgres://oussama:oussama@localhost:5432/sample"


def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parser will exit if it recieves a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])


def test_parser_with_unkown_driver(parser):
    "the parser will exist with an unkown driver"
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", "some_path"])


def test_parser_with_correct_drivers(parser):
    for driver in ["s3", "local"]:
        args = parser.parse_args([url, "--driver", driver, "/some/path"])
        assert args.url == url
        assert args.driver == driver
        assert args.destination == "/some/path"


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it recieves a driver and a destination
    """
    args = parser.parse_args([url, "--driver", "local", "/some/path"])
    assert args.url == url
    assert args.driver == "local"
    assert args.destination == "/some/path"
