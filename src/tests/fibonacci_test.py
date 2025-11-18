from src.main import fibonacci
from pytest import raises


class TestFibonacci:
    def test_0(self):
        test_val = 0
        assert fibonacci(test_val) == 0

    def test_1(self):
        test_val = 1
        assert fibonacci(test_val) == 1

    def test_5(self):
        test_val = 5
        assert fibonacci(test_val) == 5

    def test_10(self):
        test_val = 10
        assert fibonacci(test_val) == 55

    def test_neg_1(self):
        test_val = -1
        with raises(ValueError):
            fibonacci(test_val)
