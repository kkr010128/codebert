a,b=map(int,input().split())

s=[''.join([str(a)]*b),''.join([str(b)]*a)]

print(sorted(s)[0])