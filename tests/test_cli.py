import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from typer.testing import CliRunner
from app.cli import cli


def test_health_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['health'])
    assert result.exit_code == 0
