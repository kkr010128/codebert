a, b = map(int,input().split())
c = str(a) * b
d = str(b) * a
L = []
L += c,d
L = sorted(L) 
print(L[0])
