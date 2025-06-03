n = int(input())

S=[]
for i in range(n):
    S.append(input())
    
S.sort()
c=1
for i in range(n-1):
    if S[i]!=S[i+1] :
        c+=1
print( c )