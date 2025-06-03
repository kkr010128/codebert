N,M = map(int,input().split())
N_High =list(map(int,input().split()))
N_Dict = {}
for i in range(M):
    a,b = map(int,input().split())
    if N_High[a-1] == N_High[b-1]:
        N_Dict[a] = 1
        N_Dict[b] = 1
    elif N_High[a-1] > N_High[b-1]:
        N_Dict[b] = 1
    elif N_High[a-1] < N_High[b-1]:
        N_Dict[a] = 1

print(N-len(N_Dict))