# System Patterns

## Architecture Overview

code2prompt-cli follows a command-line interface (CLI) architecture pattern, designed as a Python application that processes command-line arguments and generates structured output for LLM consumption.

## Key Technical Decisions

1. **CLI-First Design**: Pure command-line interface with no GUI components
2. **Python SDK Integration**: Leverages the code2prompt Python SDK for core functionality
3. **Clipboard Integration**: Automatic clipboard copying for seamless workflow
4. **Flexible Output Formats**: Support for markdown, JSON, and XML output formats
5. **Git Integration**: Built-in support for git diffs and logs

## Design Patterns in Use

### Command Pattern
- Central CLI command (`c2p`) that processes user prompts and options
- Clear separation between command parsing and business logic

### Builder Pattern
- Incremental construction of prompts with various context elements
- Flexible inclusion/exclusion of codebase elements

### Template Pattern
- Support for custom Handlebars templates
- Default template structure with extensibility

## Component Relationships

```
User Input (CLI Args) → Command Parser → Context Generator → Prompt Builder → Output Handler
                                    ↓
                            Code2Prompt SDK
```

## Critical Implementation Paths

1. **Command Line Parsing**: Processing user options and arguments
2. **Codebase Analysis**: Scanning and filtering files based on patterns
3. **Context Assembly**: Combining file contents, directory trees, and metadata
4. **Prompt Generation**: Structuring output with LLM instructions
5. **Output Delivery**: Clipboard copying and file output options

## Data Flow

1. User executes `c2p` with options and prompt
2. CLI parses arguments and validates input
3. File system is scanned based on include/exclude patterns
4. Codebase context is assembled (files, tree structure, git info)
5. Prompt is generated with user instructions and code context
6. Output is delivered to clipboard and/or file
