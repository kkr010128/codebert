r,c=map(int,input().split())
mat = [ list(map(int,input().split())) for _ in range(0,r) ]
for xs in mat: xs.append(sum(xs))
ll = [ sum([ xs[i] for xs in mat ]) for i in range (0,c+1) ]
for xs in mat: print(' '.join(map(str,xs)))
print(' '.join(map(str,ll)))