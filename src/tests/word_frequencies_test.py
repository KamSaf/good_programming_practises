from src.main import word_frequencies


class TestWordFrequencies:
    def test_to_be_or_not_to_be(self):
        test_string = "To be or not to be"
        assert word_frequencies(test_string) == {"to": 2, "be": 2, "or": 1, "not": 1}

    def test_hello_hello(self):
        test_string = "Hello, hello!"
        assert word_frequencies(test_string) == {"hello": 2}

    def test_empty(self):
        test_string = ""
        assert word_frequencies(test_string) == {}

    def test_python_python_python(self):
        test_string = "Python python python"
        assert word_frequencies(test_string) == {"python": 3}

    def test_ala_ma_kota(self):
        test_string = "Ala ma kota, a kot ma Ale."
        assert word_frequencies(test_string) == {
            "ala": 1,
            "ale": 1,
            "ma": 2,
            "kota": 1,
            "a": 1,
            "kot": 1,
        }
