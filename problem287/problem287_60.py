# 問題: https://atcoder.jp/contests/abc144/tasks/abc144_b

n = int(input())
has_multiple = False
for a in range(1, 10):
    if n % a > 0:
        continue
    b = n / a
    if 0 < b < 10:
        has_multiple = True
        break

if has_multiple:
    print('Yes')
else:
    print('No')
