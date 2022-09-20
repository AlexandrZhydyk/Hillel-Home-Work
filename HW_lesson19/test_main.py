import unittest

from main import *


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fib_instance = Fibonacci()

    def test_fibonacci_basic(self):
        self.assertEqual(self.fib_instance(0), 0)
        self.assertEqual(self.fib_instance(1), 1)
        self.assertEqual(self.fib_instance(10), 55)

    def test_fibonacci_cache(self):
        self.assertEqual(self.fib_instance.cache, [0, 1])
        self.fib_instance(1)
        self.assertEqual(self.fib_instance.cache, [0, 1])
        self.fib_instance(9)
        self.assertEqual(self.fib_instance.cache, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fibonacci_errors(self):
        with self.assertRaises(TypeError):
            self.fib_instance()
        with self.assertRaises(TypeError):
            self.fib_instance(1, 2)
        with self.assertRaises(ValueError):
            self.fib_instance(-2)
        with self.assertRaises(ValueError):
            self.fib_instance(2.5)
        with self.assertRaises(ValueError):
            self.fib_instance("str")


class TestFormattedName(unittest.TestCase):
    def test_formatted_name_basic(self):
        self.assertEqual(formatted_name('', ''), ' ')
        self.assertEqual(formatted_name('Ivan', 'Monets'), 'Ivan Monets')
        self.assertEqual(formatted_name('ivan', 'monets'), 'Ivan Monets')
        self.assertEqual(formatted_name('ivan', 'monets', 'andriyovych'), 'Ivan Andriyovych Monets')

    def test_formatted_name_errors(self):
        with self.assertRaises(TypeError):
            formatted_name()
        with self.assertRaises(TypeError):
            formatted_name(0, 2)
        with self.assertRaises(TypeError):
            formatted_name('Anton')
        with self.assertRaises(TypeError):
            formatted_name('ivan', 'monets', 2)


if __name__ == '__main__':
    unittest.main()
