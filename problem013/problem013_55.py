N=int(input())
R=[int(input()) for i in range(N)]
S=[0 for i in range(N)]
S[0]=R[0]
for i in range(1,N):
    S[i]=min(S[i-1],R[i])
T=[R[i+1]-S[i] for i in range(N-1)]
print(max(T))

