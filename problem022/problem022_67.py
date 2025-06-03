
n=int(input())
lista=[0 for i in range(n)]
lista=input().split()
n2=int(input())
listb=[0 for i in range(n2)]
listb=input().split()
cnt=0
for i in range(n2):
    x=0
    
    for j in range(n):
        if listb[i]==lista[j] and x==0:
            x=1
            cnt+=1

print(cnt)
