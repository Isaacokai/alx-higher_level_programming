#!/usr/bin/python
import random
number = random.randint(-10000, 10000)
Number = str(number)
Number2 = Number[-1]
Number3 = int(Number2)
if (Number3 > 5):
    b = "and is greater than 5"
elif (Number3 == 0):
    b = "and is 0"
else:
    b = "and is less than 6 and not 0"
print(f"Last digit of {number} is {Number3} {b}")
