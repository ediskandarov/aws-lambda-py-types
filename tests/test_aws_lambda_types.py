from aws_lambda_types import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"
