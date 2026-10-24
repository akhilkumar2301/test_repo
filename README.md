# Deliberately Buggy Python Test Repository

This minimal repository contains a Python backend example with intentional
security and resource-management defects. It is intended for local scanner,
code-review, and test-pipeline experiments.

See [ISSUES.md](ISSUES.md) for the exact locations and root causes of the
planted bugs. Do not use these examples in production.

## Installation

Install test dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the application

```bash
python backend/app.py alice
```

## Run tests

```bash
pytest
```

The regression tests intentionally fail against the current backend
implementation to expose the known defects documented in `ISSUES.md`.
