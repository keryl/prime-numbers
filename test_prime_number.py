import unittest
import prime_numbers

class TestIsPrimeNumber(unittest.TestCase):

    def test_returns_false_if_number_is_less_than_2(self):

        for num in [-1, 0, 1]:
            self.assertEqual(prime_numbers.is_prime_number(num), False)

    def test_works_with_the_first_prime_number(self):

        self.assertEqual(prime_numbers.is_prime_number(2), True)

    def test_it_works(self):

        self.assertEqual(prime_numbers.is_prime_number(10), False)
        self.assertEqual(prime_numbers.is_prime_number(7), True)

class TestGetPrimeNumbers(unittest.TestCase):

    def test_it_rejects_numbers_below_2(self):

        for num in [-1, 0, 1]:
            self.assertEqual(prime_numbers.get_prime_numbers(num), "Number should be greater than or equal 2")

    def test_works_with_the_first_prime_number(self):

        self.assertEqual(prime_numbers.get_prime_numbers(2), [2])

    def test_it_works(self):

        self.assertEqual(prime_numbers.get_prime_numbers(10), [2, 3, 5, 7])


if __name__ == "__main__":
    unittest.main()
