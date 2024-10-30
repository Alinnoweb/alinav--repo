
def is_even(number: int) -> bool:
    """Проверяет, является ли число четным."""
    return number % 2 == 0


import unittest

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4), "4 должно быть четным числом")

    def test_odd_number(self):
        self.assertFalse(is_even(5), "5 должно быть нечетным числом")

    def test_zero(self):
        self.assertTrue(is_even(0), "0 должно быть четным числом")

    def test_negative_even_number(self):
        self.assertTrue(is_even(-2), "-2 должно быть четным числом")

    def test_negative_odd_number(self):
        self.assertFalse(is_even(-3), "-3 должно быть нечетным числом")

if __name__ == "__main__":
    unittest.main()
