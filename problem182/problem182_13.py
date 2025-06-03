n, k, c = map(int, input().split())
s = input()

l = [0 for i in range(k+1)]
r = [0 for i in range(k+1)]

cnt = 0
kaime = 1
for i in range(n):
    if kaime > k: break
    if cnt > 0:
        cnt -= 1
    else:
        if s[i] == 'o':
            l[kaime] = i
            kaime += 1
            cnt = c

cnt = 0
kaime = k
for j in range(n):
    i = n-1 - j
    if kaime < 1: break
    if cnt > 0:
        cnt -= 1
    else:
        if s[i] == 'o':
            r[kaime] = i
            kaime -= 1
            cnt = c

for i in range(1, k+1):
    if l[i] == r[i]:
        print(l[i]+1)