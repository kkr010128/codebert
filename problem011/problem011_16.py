A = list(map(int,input().split()))
a=A[0]
b=A[1]
if a<b:
    a,b=b,a
while b:
    a,b=b,a%b
print(a)