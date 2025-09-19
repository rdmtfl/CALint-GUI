from calint.entities import Report
from calint.entities.local_config import LocalConfig
from calint.use_cases.ports import LintPort, PrinterPort


def lint(linter: LintPort, config: LocalConfig, output: PrinterPort) -> Report:
    report = linter.get_lint_output(config)

    # fill in layer info
    for r in report.broken_rules:
        start_layer = config.find_layer(r.start)
        end_layer = config.find_layer(r.end)
        r.start.layer = start_layer
        r.end.layer = end_layer

    output.show(report)
    return report
