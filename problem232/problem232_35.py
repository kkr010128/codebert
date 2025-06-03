a, b = map(int, input().split())
A=''
B=''
for i in range(b):
    A+=str(a)
for i in range(a):
    B+=str(b)
if A<=B:
    print(A)
else:
    print(B)
