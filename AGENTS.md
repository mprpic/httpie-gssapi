# Development Guide

Read README.md to learn about this project.

This document describes how to work with the httpie-gssapi project.

## Project Structure

```text
src/httpie_gssapi/
└── __init__.py      # GSSAPIAuthPlugin, registered via the httpie.plugins.auth.v1 entry point

tests/
└── test_plugin.py   # Plugin registration and environment variable handling
```

## Setup

`requests-gssapi` depends on `gssapi`, which has no Linux wheels and is compiled against the system
Kerberos libraries. Install `krb5-devel` (Fedora) or `libkrb5-dev` (Debian/Ubuntu) and a C compiler
first, then:

```bash
uv sync
```

## Running All Checks with Tox

```bash
tox
```

This runs:

- Tests on Python 3.11, 3.12, 3.13, and 3.14
- Linting with ruff
- Format checking with ruff
- Type checking with ty

### Running Specific Tox Environments

```bash
tox -e py314         # Tests on a single Python version
tox -e lint          # Linting only
tox -e check-format  # Format check only
tox -e typecheck     # Type checking only
tox -e lint-fix      # Auto-fix linting issues
tox -e format        # Auto-format code
```

## Releasing

Run `make bump-minor` or `make bump-major` to bump the version, commit, tag, and (optionally) push.
Pushing a version tag triggers the `publish.yml` workflow, which publishes to PyPI via trusted
publishing.
