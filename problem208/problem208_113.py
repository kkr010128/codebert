N, M = map(int, input().split())
s = []
c = []
for _ in range(M):
    si, ci = map(int, input().split())
    s.append(si)
    c.append(ci)

for i in range(0, 999):
    i = str(i)
    if len(i) == N:
        tf = True
        for j in range(M):
            if i[s[j] - 1] != str(c[j]):
                tf = False
                break
        if tf == True:
            print(i)
            exit()

print(-1)
