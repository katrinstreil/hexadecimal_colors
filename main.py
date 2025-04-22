from color import Color
from color_analyser import ColorAnalyser

print("Example color:")
purple = Color("#8B008B")
print(purple)
print()

color_list = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
print(f"finding the brightest color from this list: {color_list} ...")
canalyser = ColorAnalyser(color_list)
brightest_color = canalyser.find_brightest_color()
print(f"The brightest color is: {brightest_color}")
