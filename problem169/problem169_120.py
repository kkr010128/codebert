n = int(input())
a = list(map(int,input().split()))
d = {}
for i in range(1,n+1):
    if i not in d:
        d[i] = 0

for i in range(len(a)):
    d[a[i]] += 1

for i in range(1,n+1):
    print(d[i])