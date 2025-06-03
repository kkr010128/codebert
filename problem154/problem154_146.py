n,k = map(int,input().split())
a = [0]*n
for _ in range(k):
    kind = int(input())
    for i in list(map(int,input().split())):
        a[i-1] += 1
print(a.count(0) if 0 in a else 0) 