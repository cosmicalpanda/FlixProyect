import math
# Funtion that takes in 3 values and returns a preference key based on calculation
def calc_value(p1,p2,p3):
    key = int(p1) * int(p2) * int(p3)
    key = (key % 5) + 1
    return key