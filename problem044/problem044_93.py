a, b, c = map(int, input().split())
l = []
for i in range(1, c+1):
    if c%i==0:
        l.append(i)
res = 0
for i in range(a, b+1):
    if i in l:
        res+=1
print(res)