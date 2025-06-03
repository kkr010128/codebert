回数 = int(input())
a, b = list(map(str, input().split()))
c = ""
for i in range(回数):
    c = c + a[i]
    c = c + b[i]
print(c)