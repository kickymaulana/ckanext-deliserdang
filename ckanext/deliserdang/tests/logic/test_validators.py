"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.deliserdang.logic import validators


def test_deliserdang_reauired_with_valid_value():
    assert validators.deliserdang_required("value") == "value"


def test_deliserdang_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.deliserdang_required(None)
