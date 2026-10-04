import pytest
from httpie.plugins.registry import plugin_manager
from httpie.status import ExitStatus
from requests_gssapi import DISABLED, OPTIONAL, REQUIRED, HTTPSPNEGOAuth

from httpie_gssapi import (
    DELEGATE,
    MUTUAL_AUTH,
    OPPORTUNISTIC_AUTH,
    GSSAPIAuthPlugin,
    convert_to_bool,
)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for var in (MUTUAL_AUTH, OPPORTUNISTIC_AUTH, DELEGATE):
        monkeypatch.delenv(var, raising=False)


def test_plugin_is_registered():
    plugin_manager.load_installed_plugins()
    assert GSSAPIAuthPlugin in plugin_manager.get_auth_plugins()


@pytest.mark.parametrize("value", ["true", "TRUE", "yes", "Yes", "1"])
def test_convert_to_bool_truthy(value):
    assert convert_to_bool(value) is True


@pytest.mark.parametrize("value", ["", "no", "false", "0", "on"])
def test_convert_to_bool_falsy(value):
    assert convert_to_bool(value) is False


def test_defaults():
    auth = GSSAPIAuthPlugin().get_auth()
    assert isinstance(auth, HTTPSPNEGOAuth)
    assert auth.mutual_authentication == REQUIRED
    assert auth.opportunistic_auth is False
    assert auth.delegate is False


@pytest.mark.parametrize(
    "value, expected",
    [("required", REQUIRED), ("Optional", OPTIONAL), ("DISABLED", DISABLED)],
)
def test_mutual_auth(monkeypatch, value, expected):
    monkeypatch.setenv(MUTUAL_AUTH, value)
    assert GSSAPIAuthPlugin().get_auth().mutual_authentication == expected


def test_mutual_auth_invalid(monkeypatch, capsys):
    monkeypatch.setenv(MUTUAL_AUTH, "bogus")
    with pytest.raises(SystemExit) as exc:
        GSSAPIAuthPlugin().get_auth()
    assert exc.value.code == ExitStatus.PLUGIN_ERROR
    assert "unsupported mutual authentication type bogus" in capsys.readouterr().err


def test_opportunistic_auth_and_delegate(monkeypatch):
    monkeypatch.setenv(OPPORTUNISTIC_AUTH, "yes")
    monkeypatch.setenv(DELEGATE, "true")
    auth = GSSAPIAuthPlugin().get_auth()
    assert auth.opportunistic_auth is True
    assert auth.delegate is True
