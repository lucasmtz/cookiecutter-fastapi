"""Unit tests for {{cookiecutter.__package_name}}."""

import re

from {{cookiecutter.__package_name}} import __version__


def test_version():
    """Test that the version is correct."""
    with open("pyproject.toml", "r") as f:
        pyproject_version = re.search(r'version = "(.*)"', f.read()).group(1)

    assert pyproject_version == __version__
