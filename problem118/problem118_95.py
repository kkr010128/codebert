N = int(input())
ans = 0


def tot(x, i):
    base = x//i
    n = base*(base+1)//2
    return i*n


for i in range(1, N+1):
    ans += tot(N, i)

print(ans)
