from itertools import accumulate
import bisect
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_acc = [0] + list(accumulate(a))
b_acc = list(accumulate(b))
#print(a_acc)
#print(b_acc)

ans = 0
for an in range(n + 1):
    rem = k - a_acc[an]
    if rem < 0:
        break

    bn = bisect.bisect_right(b_acc, rem)
    #print(bn)
    ans = max(ans, an + bn)

print(ans)