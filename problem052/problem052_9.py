n = int(input())
l = []
for i in range(3, n + 1):
    if i % 3 == 0 or "3" in str(i):
        l.append(i)

print("",*l)