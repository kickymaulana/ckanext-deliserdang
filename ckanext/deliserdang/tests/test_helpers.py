"""Tests for helpers.py."""

import ckanext.deliserdang.helpers as helpers


def test_deliserdang_hello():
    assert helpers.deliserdang_hello() == "Hello, deliserdang!"
