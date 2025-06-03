import heapq
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
bef = a[0]
for i in range(1,n):
    if bef == a[i]:
        print("NO")
        break
    bef = a[i]
    if i == n-1:
        print("YES")