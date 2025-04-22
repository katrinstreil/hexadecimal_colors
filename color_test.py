import unittest
from color import Color

class TestColorParsing(unittest.TestCase):
    def test_white(self):
        c = Color("#FFFFFF")
        self.assertEqual((c.r, c.g, c.b), (255, 255, 255))

    def test_black(self):
        c = Color("#000000")
        self.assertEqual((c.r, c.g, c.b), (0, 0, 0))

    def test_arbitrary_color(self):
        c = Color("#AABBCC")
        self.assertEqual((c.r, c.g, c.b), (170, 187, 204))

    def test_lowercase(self):
        c = Color("#aabbcc")
        self.assertEqual((c.r, c.g, c.b), (170, 187, 204))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            Color("#FFF")  # too short

    def test_missing_hash(self):
        c = Color("AABBCC")
        self.assertEqual((c.r, c.g, c.b), (170, 187, 204))


if __name__ == "__main__":
    unittest.main()
