from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_add():
    assert sub(2,3) == -1
    assert sub(5,1) == 4
    assert sub(9,9) == 0