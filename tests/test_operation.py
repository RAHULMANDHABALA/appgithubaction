from src.math_operstions import add, subtract

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(1, -1) == 2
    assert subtract(-1, -1) == 0