N=int(input())

X=[0 for _ in range(N)]
Y=[0 for _ in range(N)]

INF=1e10
Zmax=-INF
Zmin=INF
Wmax=-INF
Wmin=INF


for n in range(N):
	X[n], Y[n] = map(int, input().split())
	z = X[n] + Y[n]
	w = X[n] - Y[n]

	Zmax = max( Zmax, z )
	Zmin = min( Zmin, z )
	Wmax = max( Wmax, w )
	Wmin = min( Wmin, w )

ans = max( abs(Zmax - Zmin), abs(Wmax - Wmin))

print(ans)


