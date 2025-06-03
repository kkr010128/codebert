a = int(input())
b, c = map(str, input().split())
d = ""
for i in range(0, a):
    e = b[i] + c[i]
    d += e
print(d)