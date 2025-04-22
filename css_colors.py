import requests
import math

class CSS_Colors:

    def __init__(self):
        try:
            response = requests.get("https://www.csscolorsapi.com/api/colors")
            response.raise_for_status()
            self.css_colors = response.json()["colors"]
        except Exception as e:
            print(f"Failed to fetch color data: {e}")
            self.css_colors = []

    @staticmethod
    def parse_rgb_string(rgb_str):
        r_str, g_str, b_str = rgb_str.split(",")
        return int(r_str), int(g_str), int(b_str)

    def get_closest_css_color_name(self, r, g, b):
        try:
            def distance(css_color):
                css_r, css_g, css_b = self.parse_rgb_string(css_color["rgb"])
                return math.sqrt((r - css_r) ** 2 + (g - css_g) ** 2 + (b - css_b) ** 2)

            closest_color = min(self.css_colors, key=distance)
            return closest_color["name"]

        except Exception as e:
            print(f"Failed to process color data: {e}")
            return "Unknown"
