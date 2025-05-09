import subprocess
import sys

import doctyper
from doctyper.testing import CliRunner

from docs_src.multiple_values.arguments_with_multiple_values import tutorial001 as mod

runner = CliRunner()
app = doctyper.Typer()
app.command()(mod.main)


def test_main():
    result = runner.invoke(app, ["README.md", "pyproject.toml", "woohoo!"])
    assert result.exit_code == 0
    assert "This file exists: README.md\nwoohoo!" in result.output
    assert "This file exists: pyproject.toml\nwoohoo!" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
