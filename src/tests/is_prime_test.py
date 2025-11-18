from src.main import is_prime


class TestIsPrime:
    def test_2(self):
        test_val = 2
        assert is_prime(test_val) is True

    def test_3(self):
        test_val = 3
        assert is_prime(test_val) is True

    def test_4(self):
        test_val = 4
        assert is_prime(test_val) is False

    def test_0(self):
        test_val = 0
        assert is_prime(test_val) is False

    def test_1(self):
        test_val = 1
        assert is_prime(test_val) is False

    def test_5(self):
        test_val = 5
        assert is_prime(test_val) is True

    def test_97(self):
        test_val = 97
        assert is_prime(test_val) is True
