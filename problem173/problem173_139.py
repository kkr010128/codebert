N = int(input())
s = 0
i = 1
while i <= N:
    if i % 3 != 0 and i % 5 != 0:
        s += i
    i += 1
print(s)