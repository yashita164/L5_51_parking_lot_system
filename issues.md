# Lab 5: Static Code Analysis — Issues

| Issue | Type | Line(s) in original file | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe expression evaluation | Security — Medium | 48 | `eval()` evaluated a supplied string as a Python expression, potentially executing arbitrary code. | Replaced expression evaluation with explicit arithmetic using a numeric surge multiplier. |
| Shell command execution | Security — High | 64 | `os.system()` invoked a shell to print the manifest export message. | Replaced shell execution with Python output. |
| Weak MD5 hash | Security — High | 53 | MD5 is a weak hash algorithm for security-sensitive use. | Replaced MD5 with SHA-256. |
| Insecure PIN generation | Security — Low | 57 | `random.randint()` is not designed for security-sensitive random values. | Replaced it with `secrets.randbelow()`. |
| Mutable default argument | Code quality | 15 | A default empty list could be shared across calls. | Changed the default to `None` and initialized a list inside the function. |
| Bare exception handling | Reliability | 32 | A bare `except` silently ignored all exceptions when releasing a slot. | Added slot validation and explicit return values instead of silently ignoring errors. |
| Unused imports and variables | Code quality | 4, 37, 47, 69 | The original code imported or assigned values that were not used. | Removed unused items and simplified the affected functions. |
| Naming and missing documentation | Maintainability | Multiple | Several function names did not follow snake_case, and docstrings were missing. | Renamed functions, updated call sites, and added docstrings. |
| Formatting violations | Style | Multiple | The original file contained long lines and lacked a final newline. | Reformatted the source and added the required newline. |
| File handling and resource management | Reliability | 61–64 | The manifest file was opened and closed manually. | Used a context manager and specified UTF-8 encoding. |

## Verification

- Original Pylint score: 4.10/10.
- Final Pylint score: 10.00/10.
- Original Bandit report: 5 findings.
- Final Bandit report: No issues identified.
- Final Flake8 report: No violations reported.