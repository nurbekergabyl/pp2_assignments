# math.py

import math
import random

# Built-in functions
numbers = [5, 10, 15]
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Abs:", abs(-20))
print("Round:", round(3.14159, 2))
print("Power:", pow(2, 3))

# Math module
print("Square root:", math.sqrt(16))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))
print("Pi:", math.pi)
print("Cos(0):", math.cos(0))

# Random module
print("Random float:", random.random())
print("Random integer:", random.randint(1, 10))

items = ["apple", "banana", "cherry"]
print("Random choice:", random.choice(items))

random.shuffle(items)
print("Shuffled list:", items)