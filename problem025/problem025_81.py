import itertools as it

n=int(input())
A=input().split()
q=int(input())
M=input().split()
ans=[]
cnt=0

A=list(map(int,A))
M=list(map(int,M))

for i in range(len(A)):
    Ac=list(it.combinations(A,i+1))
    for j in Ac:
        ans.append(sum(j))

for i in M:
    flag=0
    for j in ans:
        if i==j:
            print("yes")
            flag=1
            break
    if flag==0:
        print("no")
