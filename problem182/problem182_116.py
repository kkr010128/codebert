n, k, c = map(int, input().split())
s = input()
l = len(s) - 1
i = 0
lb = []
le = []
while i < len(s) and len(lb) < k:
    if s[i] == 'o':
        lb.append(i)
        i += c + 1
        continue
    i += 1

while l > -1 and len(le) < k:
    if s[l] == 'o':
        le.append(l)
        l -= (c + 1)
        continue
    l -= 1

le.sort()
for j in range(0, len(lb)):
    if lb[j] == le[j]:
        print(lb[j]+1)