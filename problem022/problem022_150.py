def linearSearch(A,key):
    for i in range(len(A)):
        if A[i]==key:
            return i
        else: pass
    return -1


n=int(input())
s=list(input().split())
q=int(input())
t=input().split()

cnt=0
for i in range(q):
    x=linearSearch(s,t[i])
    if x!=(-1):
        cnt+=1
        
print(cnt)

