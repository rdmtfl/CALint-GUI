from calint import cli
import pytest


def test_cli():
    cli.main("calint/.calintrc.json")
