def POW(x, n, mod): #xのn乗をmodで割った際の余りの高速計算
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans *= x%mod
        x = (x*x)%mod
        n >>= 1						#ビットシフト
    return ans

if __name__ == '__main__':
	N, K = map(int, input().split())
	lst = [0] * (K+1)
	mod = 10 ** 9 + 7

	ans = 0

	for i in range(K):
		k = K - i
		n = K // k
		v = POW(n,N,mod)
		m = 2
		while(m * k <= K):
			v -= lst[m*k]
			if v < 0:
				v += mod
			m += 1
		lst[k] = v
		v = (k * v)%mod
		ans = (ans+v)%mod

	print(int(ans))