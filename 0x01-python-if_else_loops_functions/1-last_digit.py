#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastdigit = str(number)
lastdigit = lastdigit[-1]
lastdigitt = int(lastdigit)

string = "and is less than 6 and not 0"

if lastdigitt > 5:
    string = "and is greater than 5"
elif lastdigitt == 0:
    string = "and is 0"
else:
    string
print(f"Last digit of {number} is {lastdigit} {string}")
