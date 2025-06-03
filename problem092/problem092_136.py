x, k, d = map(int, input().split())

t = min(abs(x)//d, k)
u = abs(x)-d*t
print(abs(u-d*((k-t)%2)))
