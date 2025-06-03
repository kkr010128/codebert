# https://atcoder.jp/contests/abc163/tasks/abc163_b

n, m = map(int, input().split())
a = list(map(int, input().split()))
day = sum(a)
if day <= n:
    print(n-day)
else:
    print('-1')