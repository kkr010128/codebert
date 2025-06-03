S,T=input().split()
A,B=map(int,input().split())
U=input()
if S==U:
    print('{} {}'.format(A-1,B))
else:
    print('{} {}'.format(A,B-1))