#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if number < 0:
    lastdig = lastdig * -1
print("Last digit of", number, "is", lastdig, end=' ')
if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
