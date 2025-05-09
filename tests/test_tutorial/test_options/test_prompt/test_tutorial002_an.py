import subprocess
import sys

import doctyper
from doctyper.testing import CliRunner

from docs_src.options.prompt import tutorial002_an as mod

runner = CliRunner()

app = doctyper.Typer()
app.command()(mod.main)


def test_option_lastname():
    result = runner.invoke(app, ["Camila", "--lastname", "Gutiérrez"])
    assert result.exit_code == 0
    assert "Hello Camila Gutiérrez" in result.output


def test_option_lastname_prompt():
    result = runner.invoke(app, ["Camila"], input="Gutiérrez")
    assert result.exit_code == 0
    assert "Please tell me your last name: " in result.output
    assert "Hello Camila Gutiérrez" in result.output


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--lastname" in result.output
    assert "TEXT" in result.output
    assert "[required]" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
