# Deliberately Buggy Test Repository

This minimal repository contains small Python and JavaScript examples with four
intentional security and static-analysis defects. It is intended for local
scanner, code-review, and test-pipeline experiments.

## Run locally

Python requires only the standard library:

```bash
python backend/app.py alice
```

The JavaScript file is browser code. Serve the repository with any local static
file server, open `frontend/index.html` if you add one, or load `script.js` in
a page containing an element with the id `greeting`.

See [ISSUES.md](ISSUES.md) for the exact locations and root causes of the
planted bugs. Do not use these examples in production.