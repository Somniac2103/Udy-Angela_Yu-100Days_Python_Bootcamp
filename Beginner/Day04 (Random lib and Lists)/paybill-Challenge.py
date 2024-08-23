import random
import math

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(friends[(math.floor((random.random())*len(friends)))])

print(random.choice(friends))