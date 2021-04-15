#!/usr/bin/env python

"""Tests for the {{ cookiecutter.package_name }} module.
"""
import pytest

from {{ cookiecutter.package_name }} import my_module


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_{{ cookiecutter.package_name }}(an_object):
    assert an_object == {}