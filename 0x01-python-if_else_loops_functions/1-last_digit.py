#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Number = str(number)
Number2 = Number[-1]
if (number <= 0):
    Number3 = -int(Number2)
    if (Number3 == 0):
        b = "and is 0"
        print(f"Last digit of {number} is {Number3} {b}")
    else:
        b = "and is less than 6 and not 0"
        print(f"Last digit of {number} is {Number3} {b}")
else:
    Number3 = int(Number2)
    if (Number3 > 5):
        b = "and is greater than 5"
        print(f"Last digit of {number} is {Number3} {b}")
    else:
        b = "and is less than 6 and not 0"
        print(f"Last digit of {number} is {Number3} {b}")
