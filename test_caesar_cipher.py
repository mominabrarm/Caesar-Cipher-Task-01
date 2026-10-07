import unittest
from caesar_cipher import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt("HELLO", 3), "KHOOR")

    def test_decrypt(self):
        self.assertEqual(decrypt("KHOOR", 3), "HELLO")

    def test_lowercase(self):
        self.assertEqual(encrypt("hello", 3), "khoor")

    def test_spaces_and_symbols(self):
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")

    def test_wrap_around(self):
        self.assertEqual(encrypt("XYZ", 3), "ABC")

    def test_large_shift(self):
        self.assertEqual(encrypt("ABC", 29), "DEF")

    def test_negative_shift(self):
        self.assertEqual(encrypt("DEF", -3), "ABC")


if __name__ == "__main__":
    unittest.main()
