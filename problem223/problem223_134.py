from itertools import accumulate
n,k = map(int,input().split())
l = [0] + list(map(int,input().split()))
for i in range(n):
    l[i+1] = (l[i+1]+1)/2
acc = list(accumulate(l))
# print(acc)
maxi = 0
for i in range(n-k+1):
    maxi = max(maxi,acc[i+k]-acc[i])
print(maxi)