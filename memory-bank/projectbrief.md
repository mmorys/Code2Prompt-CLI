# Overview

code2prompt-cli is a Python CLI application which enables a user to generate a complete LLM prompt, including context from a software codebase, to prompt LLMs without the need for an API key, simply leveraging an LLM chat interface, such as a web interface. The code leverages the [Python SDK](https://github.com/mufeedvh/code2prompt/tree/main/crates/code2prompt-python) of [code2prompt](https://github.com/mufeedvh/code2prompt) for formatting the codebase dependencies, such as code files and file trees. The CLI tool also includes within the generated prompt high level instructions for the LLM regarding using the code and asking the user to include missing context. The CLI tool takes as a positional argument the actual text prompt the user wants to ask the LLM.

A command in the CLI would look like this, where c2p is the shortcup for the Python script entrypoint:

```shell
c2p --tree -f file1.py -f foo/file2.py Implement a serialization capability to JSON for the Foo class in foo/file2.py
```

## Interface

`c2p` is the CLI command for calling the tool. It is called with the pattern `c2p [options] user_prompt`. The tool by default acts on the current directory as th codebase directory. The tool has the following options:

```
  -i, --include <INCLUDE>
          Patterns to include
  -e, --exclude <EXCLUDE>
          Patterns to exclude
      --include-priority
          Include files in case of conflict between include and exclude patterns
  -O, --output-file <OUTPUT_FILE>
          Optional output file path
  -F, --output-format <OUTPUT_FORMAT>
          Output format: markdown, json, or xml [default: markdown]
  -t, --template <TEMPLATE>
          Optional Path to a custom Handlebars template
      --full-directory-tree
          List the full directory tree
  -c, --encoding <ENCODING>
          Optional tokenizer to use for token count
      --tokens <FORMAT>
          Display the token count of the generated prompt. Accepts a format: "raw" (machine parsable) or "format" (human readable) [default: format]
  -d, --diff
          Include git diff
      --git-diff-branch <BRANCHES> <BRANCHES>
          Generate git diff between two branches
      --git-log-branch <BRANCHES> <BRANCHES>
          Retrieve git log between two branches
  -l, --line-numbers
          Add line numbers to the source code
      --absolute-paths
          If true, paths in the output will be absolute instead of relative
  -L, --follow-symlinks
          Follow symlinks
      --hidden
          Include hidden directories and files
      --no-codeblock
          Disable wrapping code inside markdown code blocks
      --no-clipboard
          Optional Disable copying to clipboard
      --no-ignore
          Skip .gitignore rules
      --sort <SORT>
          Sort order for files: one of "name_asc", "name_desc", "date_asc", or "date_desc"
  -h, --help
          Print help (see more with '--help')
  -V, --version
          Print version
```

