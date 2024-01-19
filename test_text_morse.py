import unittest
from text_morse import TextMorse

class TestTextMorse(unittest.TestCase):

    def test_text_to_morse(self):
        test_morse = ".-"
        tm = TextMorse()
        result = tm.text_to_morse()
        self.assertEqual(result,test_morse)