s = input("")
t = input("")
k = 0

if len(s) == len(t):
    s += "?"

for i in range(len(s)-len(t)):
    cnt = 0
    for j in range(len(t)):
        if t[j] == s[i+j]:
            cnt += 1
    k = max(k, cnt)

print(len(t)-k)