N, K = input().split()
N = int(N)
K = int(K)
scores = [int(s) for s in input().split()]
sums = []
k = K-1
for i in range(k,N-1):
    if(scores[i-k] < scores[i+1]):
        print("Yes")
    else:
        print("No")