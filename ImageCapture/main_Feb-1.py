# Seattle U ECE 23.3
# Jessica Bowerman
# February 1, 2023

# Imports Functions from imageCapture.py
from imageCapture import *

# Indicates file starting
print("Start")

capPhoto()

findDifference("imagesFolder/" + imageTitle + "-0.PNG",  "imagesFolder/" + imageTitle + "-1.PNG")

# Indicates file ending
print("Finished")
