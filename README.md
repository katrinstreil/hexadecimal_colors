# Brightest Color Finder

This project solves a common frontend programming task:  
**Finding the brightest color from a list of hexadecimal color values**, and identifying the most suitable **CSS color name** using an external API.

It demonstrates:
- Clean **object-oriented design** in Python
- Use of **standard Python APIs**
- Integration with a **third-party color name API**
- Comprehensive **unit testing with mocking**

---

## Features

- Converts hex colors (e.g., `#AABBCC`) to RGB
- Calculates **perceived brightness** using a weighted formula
- Finds the **brightest** color in a list
- Identifies the **closest CSS color name** using [csscolorsapi.com](https://www.csscolorsapi.com)
- Fully tested using `unittest` with **mocked API calls**

---

##  Project Structure

 ├── color.py # Color class: hex → RGB, brightness, name 
 ├── color_analyser.py # Finds the brightest color 
 ├── css_colors.py # Handles external color name matching 
 ├── main.py # Demo runner 
 ├── color_test.py # Tests for Color 
 ├── color_analyser_test.py # Tests for ColorAnalyser 
 ├── css_colors_test.py # Tests for CSS_Colors (mocked) 
 └── README.md # This file
 
---

##  Installation

Make sure you have Python 3 installed. Then install the required dependency:

```bash
pip install requests
```

---

##  Tests

python color_test.py
python color_analyser_test.py
python css_colors_test.py

