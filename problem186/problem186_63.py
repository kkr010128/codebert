k,n=map(int,input().split())
A=sorted(list(map(int,input().split())))
A.append(A[0]+k)
a=A[0]
l=[]
for i in A:
    l.append(i-a)
    a=i
print(k-max(l))