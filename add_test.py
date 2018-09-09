import pytest

import add


def test_add():
    a = 2
    b = 3
    result = add.add(a,b)
    expected = 5
    assert expected == result