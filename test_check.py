import unittest
from luhn_check_card import luhn_check

class TestLuhnCheck(unittest.TestCase):
    def test_valid_card(self):
        self.assertTrue(luhn_check("4871450093666910"))

    def test_invalid_card(self):
        self.assertFalse(luhn_check("4871450093666911"))

    def test_non_digit_characters(self):
        with self.assertRaises(ValueError):
            luhn_check("4871a50093666910")

if __name__ == "__main__":
    unittest.main()
