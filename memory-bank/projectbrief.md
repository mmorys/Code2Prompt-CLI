# Project Brief

## Project Name
code2prompt-cli

## Current Status
**Functional CLI Implementation** - Complete command-line interface with all planned features implemented and integrated with code2prompt-rs library

## Core Purpose
To create a command-line interface (CLI) tool that leverages the code2prompt-rs library to generate structured prompts for Large Language Models (LLMs) from codebase context.

## Key Requirements
1. **CLI Interface**: Command-line tool with intuitive argument parsing
2. **Codebase Context**: Generate structured context from local codebases for LLM consumption
3. **Integration**: Seamless workflow with LLM chat interfaces
4. **Cross-Platform**: Compatible with Windows and Linux

## Current Implementation State
- Complete Python package structure with src/code2prompt_cli/
- Fully implemented main.py with Click CLI framework
- pyproject.toml configuration with all required dependencies (Click, pyperclip, GitPython, Jinja2, code2prompt-rs)
- Comprehensive test suite with passing tests
- Memory Bank documentation structure established and updated
- Full CLI functionality with all planned features implemented

## Development Priority
1. Align Memory Bank documentation with actual implementation (In Progress)
2. Complete code2prompt-rs library integration
3. Enhance testing with integration tests
4. Add advanced features (configuration files, performance optimization)
5. Implement additional output formats and templates

## Success Criteria
- Functional CLI that can generate LLM prompts from codebase context
- Proper command-line argument parsing
- Integration with existing code2prompt-rs functionality
- Cross-platform compatibility and clipboard support
