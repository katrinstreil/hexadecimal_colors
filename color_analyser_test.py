import unittest
from color import Color
from color_analyser import ColorAnalyser  # Make sure you save the analyzer class in color_analyzer.py

class TestColorAnalyser(unittest.TestCase):

    def test_brightest_color_basic_case(self):
        colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
        analyzer = ColorAnalyser(colors)
        brightest = analyzer.find_brightest_color()
        self.assertIsInstance(brightest, Color)
        self.assertEqual(brightest.hex_value, "#FFFFFF")

    def test_brightest_color_all_black(self):
        colors = ["#000000", "#000000"]
        analyzer = ColorAnalyser(colors)
        brightest = analyzer.find_brightest_color()
        self.assertEqual(brightest.hex_value, "#000000")

    def test_brightest_color_all_white(self):
        colors = ["#FFFFFF", "#FFFFFF"]
        analyzer = ColorAnalyser(colors)
        brightest = analyzer.find_brightest_color()
        self.assertEqual(brightest.hex_value, "#FFFFFF")

    def test_brightest_color_tie(self):
        colors = ["#FF0000", "#00FF00"]  # Green is brighter per formula
        analyzer = ColorAnalyser(colors)
        brightest = analyzer.find_brightest_color()
        self.assertEqual(brightest.hex_value, "#00FF00")

    def test_brightest_color_lowercase_input(self):
        colors = ["#ffffff", "#123456"]
        analyzer = ColorAnalyser(colors)
        brightest = analyzer.find_brightest_color()
        self.assertEqual(brightest.hex_value, "#FFFFFF")

if __name__ == "__main__":
    unittest.main()
