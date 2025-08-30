#!/usr/bin/env python3
"""
code2prompt-cli - A CLI tool to generate LLM prompts from codebase context.

This tool leverages the code2prompt-rs library to create structured prompts
that can be used with LLM chat interfaces without requiring API keys.
"""

import click
import sys
import os
from pathlib import Path
from typing import List, Optional

try:
    from code2prompt_rs import Code2Prompt
    CODE2PROMPT_AVAILABLE = True
except ImportError:
    CODE2PROMPT_AVAILABLE = False
    print("Warning: code2prompt-rs not available. Install it to use core functionality.")

@click.command()
@click.argument('prompt_text', type=str, required=False)
@click.option('-i', '--include', multiple=True, help='Patterns to include')
@click.option('-e', '--exclude', multiple=True, help='Patterns to exclude')
@click.option('--include-priority', is_flag=True, help='Include files in case of conflict between include and exclude patterns')
@click.option('-O', '--output-file', type=click.Path(), help='Optional output file path')
@click.option('-F', '--output-format', type=click.Choice(['markdown', 'json', 'xml']), default='markdown', help='Output format')
@click.option('-t', '--template', type=click.Path(exists=True), help='Optional Path to a custom template')
@click.option('--full-directory-tree', is_flag=True, help='List the full directory tree')
@click.option('-c', '--encoding', type=str, help='Optional tokenizer to use for token count')
@click.option('--tokens', type=click.Choice(['raw', 'format']), help='Display the token count of the generated prompt')
@click.option('-d', '--diff', is_flag=True, help='Include git diff')
@click.option('--git-diff-branch', nargs=2, type=str, help='Generate git diff between two branches')
@click.option('--git-log-branch', nargs=2, type=str, help='Retrieve git log between two branches')
@click.option('-l', '--line-numbers', is_flag=True, help='Add line numbers to the source code')
@click.option('--absolute-paths', is_flag=True, help='If true, paths in the output will be absolute instead of relative')
@click.option('-L', '--follow-symlinks', is_flag=True, help='Follow symlinks')
@click.option('--hidden', is_flag=True, help='Include hidden directories and files')
@click.option('--no-codeblock', is_flag=True, help='Disable wrapping code inside markdown code blocks')
@click.option('--no-clipboard', is_flag=True, help='Disable copying to clipboard')
@click.option('--no-ignore', is_flag=True, help='Skip .gitignore rules')
@click.option('--sort', type=click.Choice(['name_asc', 'name_desc', 'date_asc', 'date_desc']), help='Sort order for files')
@click.option('--path', type=click.Path(exists=True), default='.', help='Path to the codebase directory (default: current directory)')
@click.version_option()
def main(
    prompt_text: Optional[str],
    include: List[str],
    exclude: List[str],
    include_priority: bool,
    output_file: Optional[str],
    output_format: str,
    template: Optional[str],
    full_directory_tree: bool,
    encoding: Optional[str],
    tokens: Optional[str],
    diff: bool,
    git_diff_branch: Optional[tuple],
    git_log_branch: Optional[tuple],
    line_numbers: bool,
    absolute_paths: bool,
    follow_symlinks: bool,
    hidden: bool,
    no_codeblock: bool,
    no_clipboard: bool,
    no_ignore: bool,
    sort: Optional[str],
    path: str,
) -> None:
    """
    Generate an LLM prompt from codebase context.
    
    PROMPT_TEXT is the actual text prompt you want to ask the LLM.
    If not provided, only the codebase context will be generated.
    """
    
    # Validate input
    if not prompt_text and not include and not exclude:
        click.echo("Error: Please provide a prompt text or include/exclude patterns.")
        click.echo("Use --help for more information.")
        sys.exit(1)
    
    # Convert path to Path object
    codebase_path = Path(path).resolve()
    
    if not codebase_path.exists():
        click.echo(f"Error: Path '{path}' does not exist.")
        sys.exit(1)
    
    if not codebase_path.is_dir():
        click.echo(f"Error: Path '{path}' is not a directory.")
        sys.exit(1)
    
    # Display basic info
    click.echo(f"Generating prompt for codebase: {codebase_path}")
    
    # Prepare options for code2prompt-rs
    options = {
        'include_patterns': list(include) if include else [],
        'exclude_patterns': list(exclude) if exclude else [],
        'include_priority': include_priority,
        'output_format': output_format,
        'full_directory_tree': full_directory_tree,
        'line_numbers': line_numbers,
        'absolute_paths': absolute_paths,
        'follow_symlinks': follow_symlinks,
        'hidden': hidden,
        'no_codeblock': no_codeblock,
        'no_ignore': no_ignore,
    }
    
    if template:
        options['template_path'] = template
    
    if sort:
        options['sort_order'] = sort
    
    if encoding:
        options['encoding'] = encoding
    
    # Handle git-related options
    if diff:
        options['include_git_diff'] = True
    
    if git_diff_branch:
        options['git_diff_branches'] = list(git_diff_branch)
    
    if git_log_branch:
        options['git_log_branches'] = list(git_log_branch)
    
    if tokens:
        options['token_count_format'] = tokens
    
    # Generate prompt using code2prompt-rs
    try:
        if CODE2PROMPT_AVAILABLE:
            result = _generate_real_prompt(codebase_path, prompt_text, options)
        else:
            click.echo("Error: code2prompt-rs is not available. Please install it to use this tool.")
            sys.exit(1)
        
        # Handle output
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            click.echo(f"Prompt written to: {output_file}")
        else:
            click.echo(result)
        
        # Handle clipboard (if available and not disabled)
        if not no_clipboard:
            try:
                import pyperclip
                pyperclip.copy(result)
                click.echo("Prompt copied to clipboard!")
            except Exception as e:
                click.echo(f"Warning: Could not copy to clipboard: {e}")
    
    except Exception as e:
        click.echo(f"Error generating prompt: {e}")
        sys.exit(1)

def _generate_real_prompt(codebase_path: Path, prompt_text: Optional[str], options: dict) -> str:
    """
    Generate a real prompt using the code2prompt-rs library.
    
    Args:
        codebase_path: Path to the codebase directory
        prompt_text: Optional user prompt text
        options: Dictionary of options from CLI arguments
        
    Returns:
        Generated prompt string
    """
    try:
        # Map CLI options to code2prompt-rs parameters
        c2p_options = {
            'path': str(codebase_path),
            'include_patterns': options.get('include_patterns', []),
            'exclude_patterns': options.get('exclude_patterns', []),
            'include_priority': options.get('include_priority', False),
            'line_numbers': options.get('line_numbers', False),
            'absolute_paths': options.get('absolute_paths', False),
            'full_directory_tree': options.get('full_directory_tree', False),
            'code_blocks': not options.get('no_codeblock', False),
            'follow_symlinks': options.get('follow_symlinks', False),
            'include_hidden': options.get('hidden', False),
        }
        
        # Create Code2Prompt instance
        c2p = Code2Prompt(**c2p_options)
        
        # Generate prompt with optional template
        template_path = options.get('template_path')
        rendered_prompt = c2p.generate(template=template_path)
        
        # Extract the actual prompt content
        result = rendered_prompt.prompt
        
        # Add user prompt text if provided
        if prompt_text:
            result = f"{result}\n\n## User Request\n{prompt_text}\n\n## Instructions for LLM\nPlease analyze the codebase context above and respond to the user request.\nIf you need additional context or clarification, please ask the user."
        
        return result
        
    except Exception as e:
        raise Exception(f"Error generating prompt with code2prompt-rs: {str(e)}")

if __name__ == '__main__':
    main()
