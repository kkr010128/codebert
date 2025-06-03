a,b=map(int, input().split())
A = [str(b)]*a
B = [str(a)]*b

if a >= b:
    print(''.join(A))
if a < b:
    print(''.join(B))