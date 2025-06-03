n = int(input())
a = list(map(int, input().split()))

t1 = 0
t2 = sum(a)
ans = 10**18
for i in a:
    t1 += i
    t2 -= i
    ans = min(ans, abs(t1 - t2))
print(ans)
