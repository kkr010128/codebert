x, k, d = map(int, input().split())
x = abs(x)

if x >= k*d:
    print(x-k*d)
else:
    t = x//d
    t -= int(t%2 ^ k%2)
    print(min(x-d*t, abs(x-d*(t+2))))