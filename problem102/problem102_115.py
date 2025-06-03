N,K=map(int,input().split())
A=list(map(int,input().split()))

score=1
for i in range(K):
    score+=A[i]

for i in range(K,N):
    pre=score
    score-=A[i-K]
    score+=A[i]
    if score>pre:
        print("Yes")
    else:
        print("No")