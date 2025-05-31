import numpy
import pytest



def test_numpy():
    assert numpy.__version__ == "1.26.4", "Numpy version is not 1.26.4"
def test_print():
    assert print("hello world") is None, "Print function did not return None"
def test_assertion():
    with pytest.raises(AssertionError):


