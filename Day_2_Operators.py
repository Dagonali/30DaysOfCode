import math
import os
import random
import re
import sys

# Complete the solve function below.
# TODO For it to work on Hackerrank take out the 3 print statements below
print("Input the meal_cost")
meal_cost = float(input())
print("Input the tip_percentage")
tip_percent = int(input())
print("Input the tax_percentage")
tax_percent = int(input())
tip = (tip_percent/100)*meal_cost
print(tip)
tax = (tax_percent/100)*meal_cost
print(tax)
total_cost = meal_cost + tip + tax
int(round(total_cost))
print(int(round(total_cost)))
