from math import *

temp_C = float(input("Vnesi temperaturo v °C:"))
temp_F = temp_C * 9 / 5 + 32
temp_K = temp_C + 237.15
print(temp_C,"°C je enako",temp_F,"°F ali",temp_K,"°K")

temp_F = float(input("Vnesi temperaturo v °F:"))
temp_C = (temp_C - 32) / (9 / 5)
temp_K = temp_C + 237.15
print(temp_F,"°F je enako",temp_C,"°C ali",temp_K,"°K")
