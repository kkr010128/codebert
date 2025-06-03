def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def prime_fact(g):
    s = {1}
    i = 2
    # N=p x qとした時、(p < q)
    # 必ず p <= root(N)
    # そのためp**2までを調べればok
    while i*i <= g:
        while g % i == 0:
            g //= i
            s.add(i)
        i += 1
    s.add(g)
    return s


a, b = map(int, input().split())
G = gcd(a, b)
print(len(prime_fact(G)))
