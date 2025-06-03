import itertools


n_even, n_odd = map(int, input().split())

# 偶数になるのは、(偶数+偶数) と (奇数+奇数)
count1 = len(list(itertools.combinations(range(n_even), r=2)))
count2 = len(list(itertools.combinations(range(n_odd), r=2)))

print(count1 + count2)
