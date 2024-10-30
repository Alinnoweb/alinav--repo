
def is_even(number: int) -> bool:
    """Проверяет, является ли число четным."""
    return number % 2 == 0

def is_prime(number: int) -> bool:
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(number: int) -> int:
    """Вычисляет факториал числа."""
    if number < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


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


class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(7), "7 должно быть простым числом")

    def test_non_prime_number(self):
        self.assertFalse(is_prime(4), "4 не должно быть простым числом")

    def test_one(self):
        self.assertFalse(is_prime(1), "1 не должно быть простым числом")

    def test_zero(self):
        self.assertFalse(is_prime(0), "0 не должно быть простым числом")

    def test_negative_number(self):
        self.assertFalse(is_prime(-5), "-5 не должно быть простым числом")

class TestFactorial(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1, "Факториал 0 должен быть 1")

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120, "Факториал 5 должен быть 120")

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1, "Факториал 1 должен быть 1")

    def test_negative_number(self):
        with self.assertRaises(ValueError, msg="Факториал не определен для отрицательных чисел"):
            factorial(-3)

if __name__ == "__main__":
    unittest.main()
