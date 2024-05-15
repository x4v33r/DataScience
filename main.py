import os
import sys


numbers = [1, 2, 3, 4]
values = ["one", "two", "three", "four"]


pairs = [(number, value) for number, value in zip(numbers, values)]


print(pairs)
