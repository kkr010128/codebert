n, k = map(int, input().split())
h = [int(i) for i in input().split()]
new_h = sorted(h)[:n - k]
if n > k:
    print(sum(new_h))
else:
    print(0)