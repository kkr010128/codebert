N = int(input())

c = input()

l = len(c)
a = 0
b = 0

for i in range(l):
    if c[i] == "R":
        a += 1

for i in range(a, l):
    if c[i] == "R":
        b += 1

print(b)