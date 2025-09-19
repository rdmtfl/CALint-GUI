from abc import abstractmethod


from calint.entities import LocalConfig, Report
from calint.use_cases.ports import LintPort


class LinterAdapter(LintPort):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def lint(self, config: LocalConfig) -> Report:
        raise "method not implemented"

    @classmethod
    def get_lint_output(cls, config: LocalConfig) -> Report:
        return cls.lint(cls, config)
