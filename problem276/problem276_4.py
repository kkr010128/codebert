from itertools import accumulate


n = int(input())
a = list(map(int, input().split()))
a_acc = list(accumulate(a))
ans = 2020202020
for i in range(n):
    ans = min(abs(a_acc[-1] - a_acc[i] - a_acc[i]), ans)
print(ans)
