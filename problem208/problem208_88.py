n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

s = 10**(n-1)
if s == 1:
    s = 0
for i in range(s, 10**n):
    a = list(map(int, list(str(i))))
    for j in sc:
        if a[j[0]-1] != j[1]:
            break
    else:
        print(i)
        exit()
print(-1)