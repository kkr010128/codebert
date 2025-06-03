K,N = map(int,input().split())
A = list(map(int,input().split()))
tmin = 2*K
for i in range(1,N):
    tmin = min(tmin,K-(A[i]-A[i-1]))
tmin = min(tmin,A[N-1]-A[0])
print(tmin)