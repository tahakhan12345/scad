import pytest

from main import add

def test_add():
    assert add(5,3)==5
    assert add(-1,1)==0
    assert add(0,0)==0
