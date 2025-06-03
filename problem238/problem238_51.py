n,k,s=map(int,input().split())
L=[s]*k+[min(s+1,10**9-1)]*(n-k)
print(' '.join(map(str,L)))