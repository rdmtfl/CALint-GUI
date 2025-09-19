from calint.frameworks import JsonSerializer, ImportLinter, ClickReportPrinter
from calint.use_cases import create_config, lint


DEFAULT_CONFIG_FILE = ".calintrc.json"

# pass path as argv
def main(config_file=DEFAULT_CONFIG_FILE):
    config = create_config(JsonSerializer, config_file)

    lint(ImportLinter(), config, ClickReportPrinter())


if __name__ == "__main__":
    main(DEFAULT_CONFIG_FILE)
