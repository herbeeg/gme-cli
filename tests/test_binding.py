import pytest
import python_example as m
import new_example as n

class TestBindings:
    def testExamplePybind11Calls(self):
        assert '0.0.1' == m.__version__
        assert 3 == m.add(1, 2)
        assert -1 == m.subtract(1, 2)

    def testNewExampleBinding(self):
        assert 5 == n.new_add(2, 3)
