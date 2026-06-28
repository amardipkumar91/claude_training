---
name: python-project
description: Coding standards and project conventions for this Python project.
---

# Python Project Guidelines

This repository is a Python 3.12 application.

## Coding Standards

- Follow PEP 8.
- Use type hints for all functions.
- Add docstrings for public functions.
- Prefer small, reusable functions.
- Avoid duplicate code.
- Use f-strings instead of string concatenation.
- Use logging instead of print().

## Testing

- Every new function must have at least one pytest test.
- Tests belong in the tests/ directory.
- Name test files `test_<module>.py`.
- Test happy paths and error cases.

## Project Structure

calculator.py
- Contains business logic.

app.py
- Entry point.

tests/
- Contains pytest test cases.

## Before Completing a Task

Always:

1. Run `pytest`
2. Ensure all tests pass.
3. Check formatting.
4. Explain what files were modified.