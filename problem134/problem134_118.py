N = int(input())
A = list(map(int, input().split()))
A.sort()
res = 1
for i in A:
    res*=i;
    if res>10**18:
        res = -1
        break
print(res)