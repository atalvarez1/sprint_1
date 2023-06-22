import pytest
from bloomdata.bloomdata_functions import increment


def test_increment_int():
    assert increment(3) == 4


def test_increment_float():
    assert increment(1.5) == 2.5


def test_increment_int_return_type():
    assert isinstance(increment(3), int)