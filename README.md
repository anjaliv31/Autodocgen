# AutoDocGen

Documentation often becomes outdated as code changes.  
Most tools can generate documentation, but very few can detect when documentation
no longer matches the actual code.

AutoDocGen is an open-source tool that:

- Analyzes Python source code
- Analyzes existing documentation (docstrings)
- Detects documentation drift
- Reports issues while keeping humans in the loop

---

## Problem

In real-world codebases, functions are frequently modified,
but documentation is rarely updated at the same pace.
This leads to incorrect usage, confusion for contributors,
and avoidable bugs.

There is currently no simple automated way to **detect**
when documentation becomes outdated as code evolves.

---

## Goal

Build a tool that automatically detects mismatches between
Python code and its documentation, starting with
**parameter-level documentation drift**.

---

## How It Works

1. Reads Python function definitions to extract actual parameters.
2. Reads docstrings associated with each function.
3. Extracts parameter names mentioned in documentation.
4. Compares code parameters with documented parameters.
5. Reports mismatches as clear warnings.

---

## Example

### Input
```python
def login(username, password):
    """
    Args:
        username: user name
    """
    pass
```




## Output

⚠️ login(): parameter 'password' missing in documentation


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
