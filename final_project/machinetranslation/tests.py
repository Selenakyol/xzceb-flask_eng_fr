import unittest

from translator import englishToFrench, frenchToEnglish

class TestMyTranslation(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(" "), " ")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(" "), " ")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

unittest.main()