a,b,n = map(int,input().split())

print(int(a*(b-1)/b) if n >= b else int(a*n/b))