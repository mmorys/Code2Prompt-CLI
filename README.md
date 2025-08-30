# code2prompt-cli

A command-line interface (CLI) tool to generate structured LLM prompts from codebase context using the [code2prompt](https://github.com/mufeedvh/code2prompt) library.

## Overview

`code2prompt-cli` enables developers to efficiently provide codebase context to Large Language Models (LLMs) through chat interfaces without requiring API keys. It generates well-structured prompts that include relevant code context, making it easy to ask LLMs questions about your codebase.

## Features

- **Codebase Context Generation**: Automatically include relevant files and directory structure
- **Flexible Filtering**: Include/exclude files using glob patterns
- **Multiple Output Formats**: Markdown, JSON, and XML support
- **Clipboard Integration**: Automatic copying to clipboard for seamless workflow
- **Git Integration**: Include git diffs and commit history
- **Custom Templates**: Use your own prompt templates
- **Cross-Platform**: Works on Windows and Linux

## Installation

```bash
# Install from PyPI (when available)
pip install code2prompt-cli

# Or install in development mode
pip install -e .
```

## Usage

### Basic Usage

```bash
# Generate a prompt with a specific request
code2prompt-cli "Implement a serialization capability to JSON for the Foo class"

# Specify a codebase path
code2prompt-cli --path /path/to/project "Explain the architecture of this project"

# Include specific files only
code2prompt-cli -i "*.py" -i "*.md" "Document the Python API"
```

### Advanced Filtering

```bash
# Exclude test files and build directories
code2prompt-cli -e "test*" -e "build/*" -e "*.log" "Analyze the core functionality"

# Include priority (include overrides exclude)
code2prompt-cli -i "*.py" -e "*.py" --include-priority "Include all Python files"

# Show full directory tree
code2prompt-cli --full-directory-tree "Review the project structure"
```

### Git Integration

```bash
# Include git diff
code2prompt-cli -d "Explain the recent changes"

# Compare branches
code2prompt-cli --git-diff-branch main feature-branch "Compare these branches"

# Get commit history
code2prompt-cli --git-log-branch main feature-branch "Show commit history"
```

### Output Options

```bash
# Save to file
code2prompt-cli -O prompt.md "Generate documentation"

# Different output formats
code2prompt-cli -F json "Generate JSON format prompt"

# Custom template
code2prompt-cli -t my-template.hbs "Use custom template"

# Disable clipboard copying
code2prompt-cli --no-clipboard "Don't copy to clipboard"
```

## Options

```
Options:
  -i, --include TEXT              Patterns to include
  -e, --exclude TEXT              Patterns to exclude
  --include-priority              Include files in case of conflict between
                                  include and exclude patterns
  -O, --output-file PATH          Optional output file path
  -F, --output-format [markdown|json|xml]
                                  Output format [default: markdown]
  -t, --template PATH             Optional Path to a custom Handlebars template
  --full-directory-tree           List the full directory tree
  -c, --encoding TEXT             Optional tokenizer to use for token count
  --tokens [raw|format]           Display the token count of the generated
                                  prompt
  -d, --diff                      Include git diff
  --git-diff-branch TEXT...       Generate git diff between two branches
  --git-log-branch TEXT...        Retrieve git log between two branches
  -l, --line-numbers              Add line numbers to the source code
  --absolute-paths                If true, paths in the output will be
                                  absolute instead of relative
  -L, --follow-symlinks           Follow symlinks
  --hidden                        Include hidden directories and files
  --no-codeblock                  Disable wrapping code inside markdown code
                                  blocks
  --no-clipboard                  Disable copying to clipboard
  --no-ignore                     Skip .gitignore rules
  --sort [name_asc|name_desc|date_asc|date_desc]
                                  Sort order for files
  --path PATH                     Path to the codebase directory (default:
                                  current directory)
  --version                       Show the version and exit.
  --help                          Show this message and exit.
```

## Development

### Prerequisites

- Python 3.12+
- uv for package management

### Setup

```bash
# Clone the repository
git clone https://github.com/mmorys/code2prompt-cli.git
cd code2prompt-cli

# Install dependencies
uv sync

# Install in development mode
pip install -e .
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_cli.py
```

## Current Status

The CLI is fully functional with all planned command-line options implemented. Key features include:

- ✅ Complete argument parsing with Click
- ✅ File filtering with include/exclude patterns
- ✅ Directory tree generation
- ✅ Clipboard integration
- ✅ Output file support
- ✅ Git integration options (diff, log, branch comparison)
- ✅ Multiple output formats
- ✅ Comprehensive test suite

The core functionality currently uses a mock implementation for codebase context generation. The next step is to integrate with the actual `code2prompt-rs` library for real codebase processing.

## Development Progress

- ✅ Phase 1: CLI structure and argument parsing - COMPLETE
- ⏳ Phase 2: Integration with code2prompt-rs - IN PROGRESS
- ⏳ Phase 3: File filtering and context assembly - IN PROGRESS
- ⏳ Phase 4: Prompt generation and output handling - IN PROGRESS
- ⏳ Phase 5: Advanced features implementation - PENDING


## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
