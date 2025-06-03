S,T = input().split()
A,B = map(int, input().split())
U = input()
ans=0
if U==S:
    ans=A-1,B
else:
    ans=A,B-1
print(' '.join(map(str,ans)))