import random
import time

random_numbers = []
count_numbers = []


for i in range(1000000):

    x = random.randint(1, 6)
    random_numbers.append(x)

print(random_numbers)

for i in range(1, 7):
    print(f"{i}: {random_numbers.count(i)} occurrences")
    count_numbers.append(random_numbers.count(i))

num_max = count_numbers.index(max(count_numbers))+1
counter_max = max(count_numbers)

print(f"The number with the most occurrences is the number {num_max} appearing {counter_max} times.")

