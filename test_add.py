# test_add.py

from app import add  # Replace 'your_module' with the actual module where the 'add' function is defined

def test_add_integers():
    assert add(2, 3) == 5  # Testing with positive integers

def test_add_negative_integers():
    assert add(-2, -3) == -5  # Testing with negative integers

def test_add_mixed_sign_integers():
    assert add(2, -3) == -1  # Testing with one positive and one negative integer

def test_add_zero():
    assert add(0, 0) == 0  # Testing with zeros
    assert add(5, 0) == 5  # Testing with zero and positive integer
    assert add(0, -5) == -5  # Testing with zero and negative integer

def test_add_floats():
    assert add(2.5, 3.5) == 6.0  # Testing with floating point numbers

def test_add_large_numbers():
    assert add(1_000_000_000, 999_999_999) == 1_999_999_999  # Testing with large numbers

def test_add_strings():
    assert add("Hello, ", "World!") == "Hello, World!"  # Testing string concatenation

def test_add_list():
    assert add([1, 2], [3, 4]) == [1, 2, 3, 4]  # Testing list concatenation

def test_add_unsupported_type():
    # Testing if adding unsupported types like a number and a list raises an error
    import pytest
    with pytest.raises(TypeError):
        add(5, [1, 2, 3])
