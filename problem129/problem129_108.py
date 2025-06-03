N = int(input())
As = list(map(int,input().split()))
As.sort()
M = 1000001
array = [0]*M
for a in As:
    if array[a] != 0:
        array[a] = 2
        continue
    for i in range(a,M,a):
        array[i] += 1

ans = 0
for a in As:
    if array[a] == 1:
        ans += 1
print(ans)
