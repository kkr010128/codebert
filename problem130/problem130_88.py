
import random

name = input()

n = random.choice(name)
    
while name.find(n) > len(name) - 3:
    n = random.choice(name)

num = name.find(n)
for i in range(3):
    print(name[num + i], end = "")