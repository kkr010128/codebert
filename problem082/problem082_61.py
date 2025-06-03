S=input()
T=input()
lenS=len(S)
lenT=len(T)
count=[]

for i in range(lenS-lenT+1):
    c=0
    for j in range(lenT):
        if T[j]!=S[i+j]:
            c=c+1
        j=j+1
    count.append(c)
    i=i+1
print(min(count))