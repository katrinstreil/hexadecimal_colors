
import math
import requests
from  css_colors import CSS_Colors

class Color:
    """
    Represents a color defined by a hexadecimal string.
    Provides RGB components, brightness, and closest CSS color name.
    """

    def __init__(self, hex_value: str):
        # normalize casing
        self.hex_value = hex_value.upper()
        self.r, self.g, self.b = self._parse_hex_to_rgb()

    def _parse_hex_to_rgb(self):
        hex_clean = self.hex_value.lstrip('#')
        if len(hex_clean) != 6:
            raise ValueError(f"Invalid hex color: {self.hex_value}")
        
        r = int(hex_clean[0:2], 16)
        g = int(hex_clean[2:4], 16)
        b = int(hex_clean[4:6], 16)
        return r, g, b

    def __str__(self):
        return f"{self.hex_value} (r={self.r}, g={self.g}, b={self.b}), called {self.closest_css_color_name}"

    @property
    def brightness(self) -> float:
        """
        Computes brightness using the formula:
        sqrt(0.241 * R^2 + 0.691 * G^2 + 0.068 * B^2)
        """
        return math.sqrt(
            0.241 * (self.r ** 2) +
            0.691 * (self.g ** 2) +
            0.068 * (self.b ** 2)
        )

    @property
    def closest_css_color_name(self):
        return CSS_Colors().get_closest_css_color_name(self.r, self.g, self.b)


