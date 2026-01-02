## AutoDocGen
Documentation often becomes outdated as code changes.
Most tools can generate documentation, but very few can detect
when documentation no longer matches the actual code.

AutoDocGen is an open-source tool that:
- Analyzes source code
- Analyzes existing documentation
- Detects documentation drift
- Suggests safe updates while keeping humans in the loop

## Problem
In real-world codebases, documentation is rarely updated every time
the code changes. This leads to incorrect usage, confusion, and bugs.
There is currently no simple automated way to detect when documentation
becomes outdated.

## Goal
Build a tool that automatically detects mismatches between code and
documentation, starting with parameter-level drift.

## MVP Scope
- Parse Python functions
- Parse docstrings
- Detect missing or extra parameters in documentation
- Print clear warnings in the terminal

## Future Work
- Severity scoring
- Real repository testing
- CI/CD integration
- GitHub Action
