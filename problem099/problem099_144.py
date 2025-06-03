import math
def possible(l, a, k):
    for x in a:
        k -= math.ceil(x/l)-1
    return k>=0

n, k = map(int, input().split())
a = [int(x) for x in input().split()]
mini = 1
maxi = 10**9+7
while(mini!=maxi):
    mid = (mini+maxi)//2
    if possible(mid, a, k):
        maxi = mid
    else:
        mini = mid + 1
print(mini)
