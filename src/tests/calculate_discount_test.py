from src.main import calculate_discount
from pytest import raises


class TestDiscount:
    def test_20(self):
        test_val = 100
        test_disc = 0.2
        assert calculate_discount(test_val, test_disc) == 80.0

    def test_0(self):
        test_val = 50
        test_disc = 0
        assert calculate_discount(test_val, test_disc) == 50.0

    def test_100(self):
        test_val = 200
        test_disc = 1
        assert calculate_discount(test_val, test_disc) == 0.0

    def test_neg_10(self):
        test_val = 100
        test_disc = -0.1
        with raises(ValueError):
            calculate_discount(test_val, test_disc)

    def test_neg_150(self):
        test_val = 100
        test_disc = -1.5
        with raises(ValueError):
            calculate_discount(test_val, test_disc)
