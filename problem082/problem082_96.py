s = input()
t = input()
l = len(s)
m = len(t)
maxi = 0
for i in range(l-m+1):
    t1 = s[i:i+m]
    x = 0
    for j in range(m):
        if t1[j] == t[j]:
            x = x + 1
    if maxi < x:
        maxi = x

mini = m - maxi

print(mini)
