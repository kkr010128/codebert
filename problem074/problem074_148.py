import sys
input = sys.stdin.readline
N, K = map(int, input().split())

MOD = 998244353

P = [tuple(map(int, input().split())) for _ in range(K)]

E = [0] * N

def update(i, v):
	while i < N:
		E[i] = (E[i] + v) % MOD
		i |= i+1

def query(i):
	r = 0
	while i > 0:
		r += E[i-1]
		i &= i-1

	return r % MOD

update(0, 1)
update(1, -1)

for i in range(N-1):
	v = query(i+1)
	for L, R in P:
		if i + L < N:
			update(i+L, v)

			if i + R + 1 < N:
				update(i+R+1, -v)


print(query(N))
