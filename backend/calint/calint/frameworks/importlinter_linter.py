from calint.adapters import LinterAdapter
from calint.entities import LocalConfig, Module, Report

import sys
import os

from importlinter.application.use_cases import create_report
from importlinter.application.user_options import UserOptions
from importlinter.application.use_cases import _register_contract_types
from importlinter.application.app_config import settings
from importlinter.adapters.building import GraphBuilder


class ImportLinter(LinterAdapter):
    def __init__(self) -> None:
        pass

    def _config(config: LocalConfig) -> UserOptions:
        sys.path.insert(0, os.getcwd())

        settings.configure(
            GRAPH_BUILDER=GraphBuilder(),
        )

        options = UserOptions(
            session_options={
                "root_packages": config.roots,
            },
            contracts_options=[
                {
                    "name": "Clean Architecture Layer",
                    "type": "layers",
                    "layers": list(map(lambda x: x.import_path, config.sort_layers())),
                }
            ],
        )

        return options

    def lint(self, config: LocalConfig) -> Report:
        # should return result, not report, so that the use case can properly orchestrate the entity
        options = self._config(config)
        _register_contract_types(options)

        il_report = create_report(options)

        invalid_chains = list(il_report.get_contracts_and_checks())[0][1].__dict__[
            "metadata"
        ]["invalid_chains"]
        report = Report()
        for invalid_chain in invalid_chains:
            for chain in invalid_chain["chains"]:
                result = chain["chain"][0]

                start_module = Module(result["importer"], None)
                end_module = Module(result["imported"], None)
                report.add_broken(start_module, end_module, result["line_numbers"][0])

        return report
