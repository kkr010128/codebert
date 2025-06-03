n, m = map(int, input().split())
a = input().split()
a_sum = 0
for b in a:
    a_sum += int(b)
if a_sum > n:
    print(-1)
else:
    print(n - a_sum)