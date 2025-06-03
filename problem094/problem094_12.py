f,h=range,input
R,C,K=map(int,h().split())
l=lambda:[-~C*[0]for i in f(R+1)]
G=l()
for i in'_'*K:r,c,v=map(int,h().split());G[r][c]=v
F=[l()for i in f(4)]
for r in f(1,R+1):
	for x in f(3):
		for c in f(1,C+1):F[x+1][r][c]=max(F[x][r][c],max(F[x][r][c-1],(x<1)*F[3][r-1][c])+G[r][c],F[x+1][r][c-1])
print(F[3][R][C])