A,B,M = map(int,input().split())
Ai = list(map(int,input().split()))
Bi = list(map(int,input().split()))
amin = min(Ai)
bmin= min(Bi)
min = amin+bmin
for i in range(M):
	xi,yi,ci = map(int,input().split())
	if Ai[xi-1] + Bi[yi-1] - ci < min:
		min = Ai[xi-1] + Bi[yi-1] - ci
print(min)