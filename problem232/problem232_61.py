a,b = map(int,input().split())


A = [str(a)*b,str(b)*a]
B = sorted(A)
print(B[0])