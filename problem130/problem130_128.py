import random

name = input()
name_lenght = len(name)

start = random.randint(0, name_lenght - 3)
end = start + 3

print(name[start:end])