import random
import time

random_numbers = []

for i in range(100000):

    x = random.randint(1, 6)
    random_numbers.append(x)
    print(x)

print(random_numbers)

for i in range(1, 7):
    print(f"{i}: {random_numbers.count(i)} occurrences")


