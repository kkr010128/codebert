cnt=0
n=int(input())
S=[0 for i in range(n)]
S=input().split()
q=int(input())
T=[0 for i in range(q)]
T=input().split()
for i in range(q):
    p=0
    for j in range(n):
        if T[i]==S[j]:
            if p==0:
                cnt+=1
                p+=1
print(cnt)
