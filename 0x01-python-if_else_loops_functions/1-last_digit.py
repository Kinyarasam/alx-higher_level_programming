#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10
message = "Last digit of"
if (number < 0):
    last_num = -last_num
print("{} {} is {} and is ".format(message, number, last_num), end="")
if (last_num > 5):
    print(f"greater than 5")
elif (last_num == 0):
    print(f"0")
elif (last_num < 6):
    print(f"less than 6 and not 0")
