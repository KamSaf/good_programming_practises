from src.main import is_palindrome


class TestPalindrome:
    def test_kajak(self):
        test_string = "kajak"
        assert is_palindrome(test_string) is True

    def test_kobyla(self):
        test_string = "kobyla"
        assert is_palindrome(test_string) is True

    def test_python(self):
        test_string = "python"
        assert is_palindrome(test_string) is True

    def test_empty(self):
        test_string = ""
        assert is_palindrome(test_string) is True

    def test_A(self):
        test_string = "A"
        assert is_palindrome(test_string) is True
