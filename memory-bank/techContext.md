# Technical Context

## Technologies Actually Used
- **Primary Language**: Python 3.12+
- **Build System**: uv (as specified in pyproject.toml)
- **Core Dependency**: code2prompt-rs>=3.2.1 (Rust-based library)
- **Package Manager**: uv

## Current Development Setup
### Prerequisites
- Python 3.12+
- uv for package management
- Git for version control

### Actual Project Structure
```
code2prompt-cli/
├── src/
│   └── code2prompt_cli/
│       ├── __init__.py (fully implemented)
│       └── main.py (complete CLI implementation)
├── tests/
│   ├── test_cli.py
│   └── test_integration.py
├── memory-bank/
├── pyproject.toml
└── README.md
```

### Build and Package Management
- **Build System**: uv_build (as specified in pyproject.toml)
- **Dependencies**: Managed via pyproject.toml
- **Entry Point**: code2prompt-cli = "code2prompt_cli:main"

## Planned Technology Integration
### CLI Framework
- **Click**: For robust command-line argument parsing

### Clipboard Handling  
- **pyperclip**: Cross-platform clipboard access

### File System Operations
- **pathlib**: Modern Python path handling
- **os**: Standard file operations

### Git Integration
- **GitPython**: For git diff and log operations

### Template Engine
- **Jinja2**: Python templating for custom prompt templates

## Technical Constraints
1. **Cross-Platform Compatibility**: Must work on Windows and Linux
2. **Minimal Dependencies**: Lightweight installation footprint
3. **Performance**: Fast execution for interactive use
4. **Security**: Safe handling of file system operations
5. **Clipboard Access**: Reliable cross-platform clipboard integration

## Current Dependencies
### Runtime Dependencies (Implemented)
- click (CLI framework) - ✅ Integrated
- pyperclip (clipboard handling) - ✅ Working
- GitPython (git integration) - ✅ Available
- Jinja2 (templating) - ✅ Available
- code2prompt-rs (core functionality) - ✅ Integrated

### Development Dependencies (Installed)
- pytest (testing) - ✅ Working
- ruff (linting) - Available via uv
- pyright (type checking) - Available via uv

### Modifying Dependencies

Never modify the `pyproject.toml` directly to add or remove dependencies. Always use the `uv` interface.
- Add dependency: `uv add newdependency`
- Remove dependency: `uv remove olddependency`
- Add development dependency: `uv add --dev newdependency`
- Remove development dependency: `uv remove --dev olddependency`

## Development Command Execution

All shell command will be run through `uv`. This will ensure that the project environment is active. For example, to run pytest, use `uv run pytest`. To run a CLI command code2prompt_cli, run `uv run code2prompt_cli`.

## Current Implementation Status
- **Package Structure**: Complete with full CLI implementation
- **Dependencies**: All planned dependencies integrated and working
- **Entry Point**: Fully implemented with complete functionality
- **CLI Framework**: Click fully integrated and functional

## Development Workflow (Completed)
1. ✅ Implement CLI argument parsing with Click
2. ✅ Integrate code2prompt-rs functionality
3. ✅ Add file filtering and context assembly
4. ✅ Implement output generation and clipboard integration
5. ✅ Add testing and documentation
