h1, m1, h2, m2, k = map(int, input().split())
a1 = 60*h1 + m1
a2 = 60*h2 + m2
duration = abs(a2-a1)
ans = duration-k
if ans > 0:
    print(ans)
else:
    print(0)