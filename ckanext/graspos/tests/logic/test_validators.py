"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.graspos.logic import validators


def test_graspos_reauired_with_valid_value():
    assert validators.graspos_required("value") == "value"


def test_graspos_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.graspos_required(None)
