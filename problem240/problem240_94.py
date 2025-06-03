N,M,*f = open(0).read().split()
N = int(N)
M = int(M)
pS = [f[i*2:i*2+2] for i in range(M)]
accepted = [0] * (N+1)
wrong = [0] * (N+1)
penalty = [0] * (N+1)
for p,S in pS:
    i = int(p)
    if accepted[i] == 0:
        if S == 'AC':
            penalty[i] = wrong[i]
            accepted[i] = 1
        else:
            wrong[i] += 1
print(sum(accepted),sum(penalty))