n = int(input())
l = list(map(int, input().split()))
s = 0
m = l[0]
for i in range(n):
    if m >= l[i]:
        m = l[i]
        s += 1
print(s)
