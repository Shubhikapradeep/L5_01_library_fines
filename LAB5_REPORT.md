# Lab 5: Static Code Analysis

## Issues identified and fixes

| Issue | Type | Description | Fix approach |
|---|---|---|---|
| Mutable default argument | Bug | Shared list could retain values across calls | Used None and initialized a fresh list |
| Bare exception | Code quality | Silenced unexpected errors | Checked for missing students and books explicitly |
| Unsafe eval | Security | Arbitrary expressions could be executed | Used a restricted rule pattern and numeric parsing |
| Negative fines | Logic | Negative overdue days produced a negative fine | Return zero for negative days |
| Global state mutation | Maintainability | Renewals changed the fine rate globally | Removed the global mutation |
| Unsafe file handling | Code quality | Files lacked context management and encoding | Used with open and UTF-8 |
| Style and documentation | Style | Missing docstrings, naming and formatting issues | Added docstrings, snake_case and consistent formatting |
| Unused import | Style | os was imported but unused | Removed unused import |

## Verification

- Initial Pylint score: 6.07/10
- Final Pylint score: 10.00/10
- Initial Bandit findings: 2
- Final Bandit findings: 0
- Final Flake8 output: no violations

## Reflection

Static analysis examines source code without executing it. Pylint checks code quality and potential programming errors, Bandit identifies common security issues, and Flake8 checks style and formatting.

This lab demonstrated how static analysis can identify unsafe evaluation, mutable defaults, overly broad exception handling, and maintainability problems. After applying fixes, I reran all three tools and verified the final results.

Static analysis improves code quality by finding issues early, encouraging consistent style, and reducing security and maintenance risks.
