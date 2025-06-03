n=int(input())
m=[];M=[]
for i in range(n):
    a,s=map(int,input().split())
    m.append(a);M.append(s)
m.sort();M.sort()
if n%2:
    print(M[n//2]-m[n//2]+1)
else:
    print(M[n//2]+M[n//2-1]-m[n//2]-m[n//2-1]+1)