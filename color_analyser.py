from color import Color

class ColorAnalyser:
	def __init__(self, hex_values):
		self.colors = [Color(_) for _ in hex_values]
		
	def find_brightest_color(self):
		brightest_color = max(self.colors, key=lambda c: c.brightness)
		return brightest_color