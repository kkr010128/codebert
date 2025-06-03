S,T=map(str, input().split())
a,b=map(int, input().split())
U = str(input())

if S == U :
    a -= 1
if T == U:
    b -= 1
print(a,b)