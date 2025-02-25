<<<<<<< HEAD
import unittest
from fibonacci import calculate_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(calculate_fibonacci(0), [])
    
    def test_fibonacci_one(self):
        self.assertEqual(calculate_fibonacci(1), [0])
    
    def test_fibonacci_two(self):
        self.assertEqual(calculate_fibonacci(2), [0, 1])
    
    def test_fibonacci_five(self):
        self.assertEqual(calculate_fibonacci(5), [0, 1, 1, 2, 3])

if __name__ == '__main__':
=======
import unittest
from fibonacci import calculate_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(calculate_fibonacci(0), [])
    
    def test_fibonacci_one(self):
        self.assertEqual(calculate_fibonacci(1), [0])
    
    def test_fibonacci_two(self):
        self.assertEqual(calculate_fibonacci(2), [0, 1])
    
    def test_fibonacci_five(self):
        self.assertEqual(calculate_fibonacci(5), [0, 1, 1, 2, 3])

if __name__ == '__main__':
>>>>>>> 8660fd8003e213d0ef34b6e19792d4ee1a76c290
    unittest.main()