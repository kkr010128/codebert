from collections import Counter

n = int(input())
a = [int(x) for x in input().split()]

arr1 = []
arr2 = []
for i in range(1, n + 1):
    arr1.append(i - a[i - 1])
    arr2.append(i + a[i - 1])
    
dis1 = Counter(arr1)
dis2 = Counter(arr2)

ans = 0
for i in dis1.keys():
    ans += dis1[i] * dis2[i]

print(ans)