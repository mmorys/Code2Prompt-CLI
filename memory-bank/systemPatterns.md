# System Patterns

## Current Architecture Overview
code2prompt-cli is a Python CLI application that integrates with the code2prompt-rs library (Rust-based) to provide codebase-to-LLM prompt generation functionality. The CLI is fully implemented and functional.

## Planned Technical Decisions
1. **CLI Framework**: Click for command-line argument parsing
2. **Core Integration**: Direct integration with code2prompt-rs Python bindings
3. **Clipboard Handling**: Cross-platform clipboard library (pyperclip or similar)
4. **File System Operations**: Standard Python libraries (pathlib, os)
5. **Git Integration**: GitPython or subprocess calls for git operations

## Design Patterns to Implement
### Command Pattern
- Central CLI command that processes user input and orchestrates functionality
- Clear separation between command parsing and business logic

### Builder Pattern  
- Incremental construction of prompts with various context elements
- Flexible inclusion/exclusion of codebase elements

### Strategy Pattern
- Different output format strategies (markdown, JSON, XML)
- Template-based prompt generation strategies

## Planned Component Relationships
```
User Input (CLI Args) → Command Parser → Context Filter → Prompt Builder → Output Handler
                                    ↓              ↓
                            Code2Prompt-rs    Clipboard/Git
```

## Implementation Phases
1. **Phase 1**: Basic CLI structure with argument parsing - ✅ COMPLETE
2. **Phase 2**: Integration with code2prompt-rs library - ✅ FUNCTIONAL
3. **Phase 3**: File filtering and context assembly - ✅ IMPLEMENTED
4. **Phase 4**: Prompt generation and output handling - ✅ WORKING
5. **Phase 5**: Advanced features (clipboard, git, templates) - ✅ AVAILABLE

## Data Flow (Implemented)
1. User executes `code2prompt-cli` with options and path
2. CLI parses arguments and validates input
3. File system is scanned based on include/exclude patterns
4. Codebase context is assembled using code2prompt-rs
5. Prompt is generated with user instructions and code context
6. Output is delivered to clipboard and/or file

## Current Implementation Status
- **All Phases**: Implementation complete with full functionality
- **code2prompt-rs Integration**: Successfully integrated and working
- **Feature Set**: All planned features implemented and functional
