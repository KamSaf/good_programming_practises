from src.main import count_vowels


class TestCountVowels:
    def test_Python(self):
        test_string = "Python"
        assert count_vowels(test_string) == 2

    def test_AEIOUY(self):
        test_string = "AEIOUY"
        assert count_vowels(test_string) == 6

    def test_bcd(self):
        test_string = "bcd"
        assert count_vowels(test_string) == 0

    def test_empty(self):
        test_string = ""
        assert count_vowels(test_string) == 0

    def test_zolw(self):
        test_string = "Próba żółwia"
        assert count_vowels(test_string) == 5
