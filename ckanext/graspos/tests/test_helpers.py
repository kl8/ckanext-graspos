"""Tests for helpers.py."""

import ckanext.graspos.helpers as helpers


def test_graspos_hello():
    assert helpers.graspos_hello() == "Hello, graspos!"
