def main():

    K = int(input())
    S = input()

    mod = pow(10, 9) + 7
    N = len(S)

    g1 = [1, 1]
    g2 = [1, 1]
    inv = [0, 1]

    for i in range(2, K+N+1):
        g1.append((g1[-1] * i) % mod)
        inv.append( ( -inv[mod % i] * (mod//i)) % mod )
        g2.append((g2[-1] * inv[-1]) % mod)

    def combi(n, r):
      r = min(r, n-r)
      return g1[n]*g2[r]*g2[n-r]%mod

    pow25 = [1]
    pow26 = [1]
    for i in range(K):
        pow25.append(pow25[-1] * 25 % mod)
        pow26.append(pow26[-1] * 26 % mod)

    ans = 0
    for i in range(N-1, N+K):
        ans += combi(i, N-1) * pow25[i-N+1] % mod * pow26[K-i+N-1] % mod
        ans %= mod
    return ans

if __name__ == '__main__':
    print(main())