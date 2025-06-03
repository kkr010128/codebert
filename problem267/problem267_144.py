n = int(input())
s = list(input())
t = []
ans = 0
for i in range(1000):
    t.append(str(i//100))
    t.append(str(i//10%10))
    t.append(str(i%10))
    k = 0
    p = 0
    for j in range(3):
        if t[j] in s[k:]:
            p = s[k:].index(t[j]) + 1
            k += p
        else:
            p = -1
            break
    if p != -1:
        ans += 1
    t.clear()
print(ans)