# Augustine
# main.py
import math
from math import sqrt
import statistics as st
import conversions
from conversions import celsius_to_fahrenheit, shillings_to_dollars
# Part 2
print(math.sqrt(225))
print(round(math.pi, 4))
print(math.ceil(7.2))
print(math.floor(7.8))
print(round(math.pi * 5 * 5, 2))
# Part 3 
temps = [24, 27, 22, 30, 25, 28, 21]
print(round(st.mean(temps), 2))
print(st.median(temps))
print(round(st.stdev(temps), 2))
print(sqrt(49))
# Part 5 
print(conversions.km_to_miles(42.195))
print(celsius_to_fahrenheit(30))
print(shillings_to_dollars(12900))
print(shillings_to_dollars(12900, 130))
# Part 6 
def make_label():
    label = "Weekly report"
    print(label)
make_label()
# label
def get_label():
    label = "Weekly report"
    return label
print(get_label())