"""
GSSAPI authentication plug-in for HTTPie.
"""

import os
import sys

from httpie.plugins import AuthPlugin
from httpie.status import ExitStatus
from requests_gssapi import DISABLED, OPTIONAL, REQUIRED, HTTPSPNEGOAuth

MUTUAL_AUTH = "HTTPIE_GSSAPI_MUTUAL_AUTH"
OPPORTUNISTIC_AUTH = "HTTPIE_GSSAPI_OPPORTUNISTIC_AUTH"
DELEGATE = "HTTPIE_GSSAPI_DELEGATE"


def convert_to_bool(value: str) -> bool:
    """Check if the value of an environment variable is truthy."""
    return value.lower() in ("true", "yes", "1")


class GSSAPIAuthPlugin(AuthPlugin):
    """GSSAPI authentication plug-in."""

    name = "GSSAPI auth"
    auth_type = "gssapi"
    auth_require = False
    auth_parse = False

    def get_auth(self, username: str | None = None, password: str | None = None) -> HTTPSPNEGOAuth:
        """Return a configured HTTPSPNEGOAuth authentication class instance."""
        mutual_auth = os.getenv(MUTUAL_AUTH, "required").lower()
        if mutual_auth == "required":
            mutual_auth = REQUIRED
        elif mutual_auth == "optional":
            mutual_auth = OPTIONAL
        elif mutual_auth == "disabled":
            mutual_auth = DISABLED
        else:
            sys.stderr.write(
                f"httpie_gssapi error: unsupported mutual authentication type {mutual_auth}\n"
            )
            sys.exit(ExitStatus.PLUGIN_ERROR)

        opportunistic_auth = convert_to_bool(os.getenv(OPPORTUNISTIC_AUTH, ""))
        delegate = convert_to_bool(os.getenv(DELEGATE, ""))

        return HTTPSPNEGOAuth(
            mutual_authentication=mutual_auth,
            opportunistic_auth=opportunistic_auth,
            delegate=delegate,
        )
