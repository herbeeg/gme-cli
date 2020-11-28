import pytest

from click.testing import CliRunner

from cli.main import default

class TestMainCLI:
    def testMainOutput(self):
        runner = CliRunner()
        result = runner.invoke(default)

        assert 0 == result.exit_code
        assert 'Welcome to the gme-cli interface. Please state your purpose.' in result.output