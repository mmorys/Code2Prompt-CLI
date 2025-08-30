# Product Context

## What This Project Is
code2prompt-cli is a command-line tool designed to bridge the gap between local codebases and Large Language Model (LLM) chat interfaces. It generates structured, copyable prompts that contain relevant code context, enabling developers to efficiently leverage LLMs for code-related tasks.

## Problems It Solves
1. **Manual Context Preparation**: Developers currently spend time manually copying and formatting code snippets for LLM queries
2. **Inefficient Workflow**: Switching between code editors and LLM chat interfaces breaks flow state
3. **Context Management**: Difficulty in selecting and presenting relevant code context to LLMs
4. **Repetitive Tasks**: Common coding questions require similar context patterns

## How It Should Work
1. **Command-Line Execution**: `code2prompt-cli [options] [path]`
2. **Flexible Filtering**: Include/exclude files via glob patterns and .gitignore integration
3. **Clipboard Integration**: Automatic copying of generated prompts to clipboard
4. **Structured Output**: Well-formatted prompts ready for LLM consumption
5. **Cross-Platform**: Consistent behavior on Windows and Linux

## User Experience Goals
- **Intuitive**: Simple commands with sensible defaults
- **Efficient**: Fast execution and minimal configuration
- **Flexible**: Powerful filtering and customization options
- **Reliable**: Consistent cross-platform behavior
- **Seamless**: Integrates naturally into development workflows

## Current State
The project is in early development with only a basic skeleton implemented. The core functionality needs to be built to match these product requirements.

## Success Metrics
- Reduces time spent preparing LLM prompts from codebases
- Increases developer efficiency in LLM-assisted coding tasks
- Provides reliable cross-platform clipboard integration
- Offers flexible codebase filtering and inclusion options
