N, X, T = (int(x) for x in input().split() )

a = int(N/X)

if N % X != 0:
    t = (a + 1)* T
else:
    t = a * T

print(t)
