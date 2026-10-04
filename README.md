# httpie-gssapi

GSSAPI authentication plug-in for [HTTPie](https://httpie.io/).

This plug-in uses the [requests-gssapi](https://github.com/pythongssapi/requests-gssapi) library,
which is a more modern replacement for the old
[requests-kerberos](https://github.com/requests/requests-kerberos) library.

## Installation

Install the plug-in using HTTPie's plug-in manager:

```bash
httpie cli plugins install httpie-gssapi
```

Or, if you installed HTTPie with `uv tool`:

```bash
uv tool install httpie --with httpie-gssapi
```

This will add the `gssapi` authentication method under `--auth-type` in the `http --help` output.

Note that `requests-gssapi` depends on [gssapi](https://pypi.org/project/gssapi/), which is
compiled against your system's Kerberos libraries. On Linux, make sure the Kerberos development
headers (e.g. `krb5-devel` on Fedora or `libkrb5-dev` on Debian/Ubuntu) and a C compiler are
installed first.

## Usage

Ensure you have a valid Kerberos ticket by running `kinit`.

```bash
http --auth-type=gssapi https://example.org
```

Note that supplying authentication credentials is not necessary, meaning the following two
commands are equivalent:

```bash
http --auth-type=gssapi https://example.org
http --auth-type=gssapi --auth : https://example.org
```

## Configuration Options

The following environment variables can be set to modify the GSSAPI authentication behavior:

- `HTTPIE_GSSAPI_MUTUAL_AUTH` (default: `required`): determines whether mutual authentication
  from the server should be required. For more information, see
  [Mutual Authentication](https://github.com/pythongssapi/requests-gssapi#mutual-authentication).
  Possible values are: `required`, `optional`, `disabled`.

- `HTTPIE_GSSAPI_OPPORTUNISTIC_AUTH` (default: `no`): enables or disables preemptively initiating
  the GSSAPI exchange. For more information, see
  [Opportunistic Authentication](https://github.com/pythongssapi/requests-gssapi#opportunistic-authentication).
  Possible values are: `yes`, `true`, `1`; all other values default to `no`.

- `HTTPIE_GSSAPI_DELEGATE` (default: `no`): enables or disables credential delegation. For more
  information, see [Delegation](https://github.com/pythongssapi/requests-gssapi#delegation).
  Possible values are: `yes`, `true`, `1`; all other values default to `no`.

## Development

Run the test suite, linter, formatter check, and type checker with:

```bash
tox
```

Releases are published to PyPI automatically when a version tag is pushed; use `make bump-minor`
or `make bump-major` to bump the version, commit, and tag.
