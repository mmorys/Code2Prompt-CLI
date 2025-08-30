# Product Context

## Purpose

code2prompt-cli exists to solve the problem of efficiently providing codebase context to Large Language Models (LLMs) through chat interfaces without requiring API keys or direct API access. It bridges the gap between local codebases and LLM capabilities by generating structured prompts that include relevant code context.

## Problem Statement

Developers frequently need to ask LLMs questions about their codebases, but manually copying and pasting code fragments is inefficient and error-prone. Existing solutions often require API keys, complex setup, or don't provide adequate context structure for LLMs to understand the codebase effectively.

## Solution Approach

code2prompt-cli generates comprehensive LLM prompts that include:
- Structured codebase context with file trees and contents
- High-level instructions for LLM usage
- Flexible filtering and formatting options
- Direct clipboard integration for seamless workflow

## User Experience Goals

1. **Simplicity**: Single command execution with intuitive options
2. **Flexibility**: Comprehensive filtering, inclusion/exclusion patterns, and output formats
3. **Efficiency**: Fast generation and automatic clipboard copying
4. **Context Awareness**: Smart handling of git diffs, line numbers, and directory structures
5. **Integration**: Seamless workflow with existing LLM chat interfaces

## Target Users

- Software developers working with LLMs for code assistance
- Teams wanting to leverage LLMs without complex API setups
- Developers needing quick codebase context generation for documentation or analysis
