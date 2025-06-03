s = input()
t = input()
ans = 1000
c = 0


for i in range(len(s)-len(t)+1):
    for j in range(len(t)):
        if s[i+j] == t[j]:
            c += 1
    ans = min(len(t) - c , ans)
    c = 0

print(ans)