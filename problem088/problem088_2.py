n = int(input())
wa = 0
m = 0
l = list(map(int, input().split()))
for i in range(n):
    m = max(l[i], m)
    if m > l[i]:
        wa += m - l[i]
print(wa)