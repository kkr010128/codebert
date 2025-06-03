f,g,h=range,max,input
R,C,K=map(int,h().split())
G=[[0]*-~C for i in f(R+1)]
for i in'_'*K:r,c,v=map(int,h().split());G[r][c]=v
F=[[[0]*-~C for i in f(R+1)]for i in f(4)]
for r in f(1,R+1):
	for x in f(1,4):
		for c in f(1,C+1):F[x][r][c]=g(F[x-1][r][c],F[x-1][r][c-1]+G[r][c],F[x][r][c-1],(x<2)*(G[r][c]+g(F[1][r-1][c],F[2][r-1][c],F[3][r-1][c])))
print(F[3][R][C])