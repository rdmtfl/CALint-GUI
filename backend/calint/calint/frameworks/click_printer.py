from click import secho
from calint.adapters import Presenter
from calint.entities import Report


class ClickReportPrinter(Presenter):
    def __init__(self) -> None:
        pass

    def present(self, report: Report):
        if not report.broken_rules:
            secho("No rules broken.", fg="green")
        else:
            for broken_rule in report.broken_rules:
                secho(
                    f"- {broken_rule.start.layer.name} ({broken_rule.start.path})"
                    f" imported {broken_rule.end.layer.name} ({broken_rule.end.path})"
                    f" at line {broken_rule.line}",
                    fg="red",
                )
            broken_rules_n = len(report.broken_rules)
            secho(f"\n{broken_rules_n} rule{'s'[:broken_rules_n^1]} broken")
