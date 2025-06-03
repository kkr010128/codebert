
n,m=map(int,input().split())
parent=[*range(n)]
sz=[1]*n


def anc(a):
	# print(a)
	if parent[a]==a:
		return a
	else:
		return(anc(parent[a]))


def union(a,b):
	pa=anc(a)
	pb=anc(b)
	if sz[pb]<sz[pa]:
		pa,pb=pb,pa
	parent[pa]=pb
	sz[pb]+=sz[pa]
	sz[pa]=0


# print(parent)
for i in range(m):
	a,b=map(int,input().split())
	a-=1
	b-=1
	if anc(a)!=anc(b):
		union(a,b)
	# print(parent,a,b)

print(max(sz))



