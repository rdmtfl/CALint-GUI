from pytest_mock import mocker
from calint.entities import Layer, LocalConfig
from calint.frameworks import ImportLinter, ClickReportPrinter, JsonSerializer
from calint.use_cases import create_config, lint


config = create_config(JsonSerializer, "calint/.calintrc.json")


def test():
    report = lint(ImportLinter, config, ClickReportPrinter)
    assert len(report.broken_rules) == 2
