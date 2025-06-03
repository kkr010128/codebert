n, x, t = map(lambda x: int(x), input().split())
if n % x == 0:
    group = n // x
else:
    group = n // x + 1
answer = group * t
print(answer)