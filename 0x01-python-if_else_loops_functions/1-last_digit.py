#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = str(number)
lastdigit = lastdigit[-1]
lastdigitt = int(lastdigit)
if number < 0:
    lastdigitt = 0 - lastdigitt

string = f"Last digit of {number} is {lastdigitt}"

if lastdigitt == 0:
    print(f"{string} and is 0")
elif lastdigitt > 5:
    print(f"{string} and is greater than 5")
else:
    print(f"{string} and is less than 6 and not 0")
