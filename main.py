from color import Color
from color_analyser import ColorAnalyser

purple = Color("#8B008B")
print(purple)

color_list = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
canalyser = ColorAnalyser(color_list)
brightest_color = canalyser.find_brightest_color()
print(f"The brightest color is: {brightest_color}")
