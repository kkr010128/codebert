from bisect import bisect_left

n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0

# a<b<c として、aとbを固定する
# 残る条件は c<a+b のみ
# aとbの固定方法がO(N^2), cの二分探索がO(logN)、結局O(N^2logN)
# 二分探索は事前にソートが必要

# ex. 2, 4(a), 4, 7(b), | 8, 9, 9 | (ここにa+b=11が挿入される), 12, 14
# cとして適切なのは8,9,9の3通り
# bisect_rightだとa+bが存在した時にバグる

for ai in range(n):
    for bi in range(ai + 1, n):
        ans += bisect_left(l, l[ai] + l[bi]) - bi - 1
print(ans)
