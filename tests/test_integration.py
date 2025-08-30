import pytest
from click.testing import CliRunner
from code2prompt_cli.main import main
import tempfile
import os
from pathlib import Path

def test_cli_with_prompt():
    """Test CLI with a simple prompt."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create a simple test file
        with open('test_file.py', 'w') as f:
            f.write('# This is a test file\nprint("Hello, World!")\n')
        
        result = runner.invoke(main, ['--path', '.', 'Analyze this code'])
        assert result.exit_code == 0
        assert 'Generating prompt for codebase' in result.output
        assert 'Source Tree' in result.output
        assert 'User Request' in result.output

def test_cli_with_output_file():
    """Test CLI with output file option."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create a simple test file
        with open('test_file.py', 'w') as f:
            f.write('# Test file content\n')
        
        result = runner.invoke(main, [
            '--path', '.',
            '--output-file', 'output.txt',
            'Test prompt'
        ])
        
        assert result.exit_code == 0
        assert 'Prompt written to: output.txt' in result.output
        assert os.path.exists('output.txt')

def test_cli_with_include_exclude():
    """Test CLI with include/exclude patterns."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create test files
        with open('include_me.py', 'w') as f:
            f.write('# This should be included\n')
        with open('exclude_me.txt', 'w') as f:
            f.write('# This should be excluded\n')
        
        result = runner.invoke(main, [
            '--path', '.',
            '--include', '*.py',
            '--exclude', '*.txt',
            'Test with patterns'
        ])
        
        assert result.exit_code == 0
        assert 'Generating prompt for codebase' in result.output
