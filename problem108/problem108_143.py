import itertools

n = int(input())

for i in itertools.count():
    if (i * 1000) >= n:
        break

print(i * 1000 - n)
