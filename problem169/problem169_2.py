n = int(input())
A = list(map(int,input().split()))

ANS=[0]*(n)
for i in range(n-1):
    a=A[i]
    ANS[a-1]+=1
for i in range(n):
    print(ANS[i])