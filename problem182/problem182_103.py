# with open('./ABC161/max_02') as f:
#     l = [s.strip() for s in f.readlines()]


n,k,c = map(int, input().split())
s = input()

l = list()
r = list()
i = 0
while i < n:
    if len(l) == k:
        break
    if s[i] == 'o':
        l.append(i)
        i += c
    i+=1

i = n-1
while i >= 0:
    if len(r) == k:
        break
    if s[i] == 'o':
        r.append(i)
        i -= c
    i-=1
r.sort()

for i in range(k):
    if l[i] == r[i]:
        print(l[i]+1)




