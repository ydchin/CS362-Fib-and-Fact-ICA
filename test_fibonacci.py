import unittest
import fibonacci
import pytest

#UnitTest
class testFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fibonacci.fibonacci(0), 0)
    def test_2(self):
        self.assertEqual(fibonacci.fibonacci(1),1)
    def test_3(self):
        with self.assertRaises(Exception):
            fibonacci.fibonacci(-1)
    def test_4(self):
        with self.assertRaises(TypeError):
            fibonacci.fibonacci("Hello")

if __name__ == '__main__':
    unittest.main(verbosity=2)


#PyTest
def test_answer1():
    assert fibonacci.fibonacci(0) == 0

def test_answer2():
    assert fibonacci.fibonacci(1) == 1

def test_answer3():
    with pytest.raises(Exception):
        fibonacci.fibonacci(-1)

def test_answer4():
    with pytest.raises(TypeError):
        fibonacci.fibonacci("Hello")