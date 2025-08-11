import funkcje
import unittest
from unittest.mock import patch
from io import StringIO

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(funkcje.add(2,4), 6)
        self.assertNotEqual(funkcje.add(2,4), 5)


class TestIfPalindrom(unittest.TestCase):
    def test_palindrom(self):
        self.assertTrue(funkcje.if_palindrom("kamilslimak"))
        self.assertEqual(funkcje.if_palindrom("ala"), True)
    def test_not_palindrom(self):
        self.assertFalse(funkcje.if_palindrom("wiadro"), False)
        self.assertEqual(funkcje.if_palindrom("kamyk"), False)


class TestIfValidTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(funkcje.if_valid_triangle(2,3,4), True)
        self.assertEqual(funkcje.if_valid_triangle(5,9,5), True)
    def test_not_valid_triangle(self):
        self.assertEqual(funkcje.if_valid_triangle(1,1,2), False)
        self.assertEqual(funkcje.if_valid_triangle(-2,0,1), False)

class TestDivideFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_divide(self, mock_stdout):
        funkcje.divide(4,2)
        self.assertEqual(mock_stdout.getvalue(), '2.0\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_divide_exception(self, mock_stdout):
        funkcje.divide(4,0)
        self.assertEqual(mock_stdout.getvalue(), 'Nie dziel przez 0\n')

class TestSortList(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(funkcje.sort_strings_by_length(['kot','pies','dziobak']), ['kot','pies','dziobak'])
    def test_reverse_list(self):
        self.assertEqual(funkcje.sort_strings_by_length(['dziobak','pies','kot']), ['kot','pies','dziobak'])
    def test_empty_list(self):
        self.assertEqual(funkcje.sort_strings_by_length([]), [])
    def test_mixed_list(self):
        self.assertEqual(funkcje.sort_strings_by_length(['kot','dziobak','pies']), ['kot','pies','dziobak'])

class TestIfPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(funkcje.if_prime(5), True)
    def test_is_not_prime(self):
        self.assertEqual(funkcje.if_prime(4), False)
    def test_1(self):
        self.assertEqual(funkcje.if_prime(1), False)
    def test_0(self):
        self.assertEqual(funkcje.if_prime(0), False)
    def test_negative(self):
        self.assertEqual(funkcje.if_prime(-1), False)

class TestCalculateMean(unittest.TestCase):
    def test_list(self):
        self.assertEqual(funkcje.calculate_mean([1,4,7]), 4)
        self.assertEqual(funkcje.calculate_mean([1,5,'kot']), -2)

    def test_empty_list(self):
        self.assertEqual(funkcje.calculate_mean([]), -1)


if __name__ == '__main__':
    unittest.main()
