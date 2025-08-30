import pytest
from click.testing import CliRunner
from code2prompt_cli.main import main

def test_cli_import():
    """Test that the CLI module can be imported."""
    assert main is not None

def test_cli_help():
    """Test that the CLI --help works."""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert 'Usage' in result.output

def test_cli_basic_execution():
    """Test basic CLI execution."""
    runner = CliRunner()
    result = runner.invoke(main, ['--path', '.', 'Test prompt'])
    assert result.exit_code == 0
    assert 'Generating prompt for codebase' in result.output
