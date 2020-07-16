import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5, 10), 15)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 10), 50)

    def test_power(self):
        self.assertEqual(katas.power(5, 10), 9765625)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(10), 34)


if __name__ == '__main__':
    unittest.main()
