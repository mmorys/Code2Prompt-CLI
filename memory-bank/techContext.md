# Technical Context

## Technologies Used

- **Primary Language**: Python
- **CLI Framework**: Click
- **Core Dependency**: code2prompt Python SDK (https://github.com/mufeedvh/code2prompt)
- **Clipboard Handling**: pyperclip or similar cross-platform library
- **File System Operations**: Standard Python libraries (os, pathlib)
- **Git Integration**: GitPython primarily, or subprocess calls to git if needed
- **Template Engine**: Handlebars (likely via a Python implementation)

## Development Setup

### Prerequisites
- Python 3.10+
- uv for package management
- Git for version control

### Project Structure
```
code2prompt-cli/
├── src/
│   └── code2prompt_cli/
│       ├── __init__.py
│       └── main.py (entry point)
├── memory-bank/
├── pyproject.toml
└── README.md
```

### Build and Package Management
- **Build System**: uv
- **Dependencies**: Managed via pyproject.toml

### Testing
- pytest test framework
- Unit tests for core functionality
- Integration tests for CLI interface

## Technical Constraints

1. **Cross-Platform Compatibility**: Must work on Windows and Linux
2. **Minimal Dependencies**: Lightweight installation footprint
3. **Performance**: Fast execution for interactive use
4. **Security**: Safe handling of file system operations
5. **Clipboard Access**: Reliable cross-platform clipboard integration

## Dependencies

### Runtime Dependencies
- code2prompt Python SDK
- Clipboard handling library
- Git integration library (if not using subprocess)

### Development Dependencies
- Project management (uv)
- Testing (pytest)
- Linting and formatting tools (ruff)
- Type checking (pyright)
- Build tools (uv)

## Tool Usage Patterns

### Development Workflow
1. Edit source files in `src/code2prompt_cli/`
2. Test locally with `python -m code2prompt_cli` or installed entry point
3. Run tests to ensure functionality
4. Use linters and formatters for code quality

### Build and Release
1. Update version in pyproject.toml
2. Build package with Poetry
3. Publish to PyPI or distribute as wheel

### Debugging
1. Use logging for CLI output, with a logger configuration defined at the entry to the application.
2. Test individual components in isolation
3. Verify clipboard functionality across platforms
