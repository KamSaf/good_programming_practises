import string


def is_palindrome(text: str) -> bool:
    lower_case_text = text.lower()
    return lower_case_text == lower_case_text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError
    if n < 3:
        return n
    vals = [1, 2]
    for i in range(2, n):
        vals.append(sum(vals[i - 2 : i]))
    return vals[n - 1]


def count_vowels(text: str) -> int:
    vowels = ("a", "e", "i", "o", "u", "y")
    counter = 0
    for c in text.lower():
        counter += 1 if c in vowels else 0
    return counter


def calculate_discount(price: float, discount: float) -> float:
    if not 0 < discount < 1:
        raise ValueError
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    new_list = []
    for el in nested_list:
        if type(el) is list:
            new_list += flatten_list(el)
        else:
            new_list.append(el)
    return new_list


def word_frequencies(text: str) -> dict:
    translator = str.maketrans("", "", string.punctuation)
    words_dict = {}
    split_text = map(lambda w: w.translate(translator).lower().strip(), text.split(" "))
    for word in split_text:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    return is_prime


print(is_prime(6))
