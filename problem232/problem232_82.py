a,b=input().split()
A=int(a)
B=int(b)
aa=a
bb=b
for i in range(B-1):
    aa+=a
for j in range(A-1):
    bb+=b
if aa >= bb:
    print(bb)
else:
    print(aa)