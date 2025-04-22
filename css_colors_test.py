import unittest
from unittest.mock import patch
from css_colors import CSS_Colors

class TestCSSColors(unittest.TestCase):

    @patch("css_colors.requests.get")
    def test_closest_color_blue(self, mock_get):
        # Mock response data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "colors": [
                {"name": "DarkMagenta", "rgb": "139,0,139"},
                {"name": "Blue", "rgb": "0,0,255"},
                {"name": "DodgerBlue", "rgb": "30,144,255"}
            ]
        }

        css = CSS_Colors()
        name = css.get_closest_css_color_name(10, 10, 250)
        self.assertEqual(name, "Blue")

    @patch("css_colors.requests.get")
    def test_closest_color_dodgerblue(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "colors": [
                {"name": "DarkMagenta", "rgb": "139,0,139"},
                {"name": "Blue", "rgb": "0,0,255"},
                {"name": "DodgerBlue", "rgb": "30,144,255"}
            ]
        }

        css = CSS_Colors()
        name = css.get_closest_css_color_name(35, 140, 250)
        self.assertEqual(name, "DodgerBlue")

    @patch("css_colors.requests.get")
    def test_closest_color_darkmagenta(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "colors": [
                {"name": "DarkMagenta", "rgb": "139,0,139"},
                {"name": "Blue", "rgb": "0,0,255"},
                {"name": "DodgerBlue", "rgb": "30,144,255"}
            ]
        }

        css = CSS_Colors()
        name = css.get_closest_css_color_name(140, 5, 140)
        self.assertEqual(name, "DarkMagenta")


if __name__ == "__main__":
    unittest.main()
