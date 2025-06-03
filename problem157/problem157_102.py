import sys
input = sys.stdin.readline
from collections import Counter


def rle(list):
    dict = {}
    for i in list:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


n = int(input())
a = list(map(int, input().split()))
minus = Counter([i-a[i] for i in range(n)])
plus = Counter([i+a[i] for i in range(n)])

cnt = 0
for i in minus:
    if i in plus:
        cnt += minus[i] * plus[i]
print(cnt)
