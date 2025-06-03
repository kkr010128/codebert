n = int(input())
a = []
for i in range(n):
    s = str(input())
    a.append(s)
b = set(a)
print(len(b))