def solve(n):
    D = {k: 0 for k in range(1, n+1)}
    m = int(n**0.5)
    for x in range(1, m+1):
        for y in range(1, m+1):
            for z in range(1, m+1):
                k = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if k <= n:
                    D[k] += 1
                else:
                    break
    for k in range(1, n+1):
        print(D[k])

n = int(input())
solve(n)

