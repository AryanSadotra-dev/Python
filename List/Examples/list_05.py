"""
Write a program to generate and store in a list 20 random numbers in the range 10 to 100.
From this list, delete all those entries which have value between 20 and 50.
Print the remaining list.
"""
#1.
import random

num = []
i = 1

# generate 20 random numbers
while i <= 20:
    ran = random.randint(10, 100)
    num.append(ran)
    i += 1

print("Original list:", num)

# delete numbers between 20 and 50
for ran in num[:]:            # looping over a copy
    if ran > 20 and ran < 50:
        num.remove(ran)

print("Remaining list:", num)
