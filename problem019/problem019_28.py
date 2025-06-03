from collections import deque
n,q = list(map(int, input().split()))
P = deque([[p,int(t)] for p,t in [input().split() for _ in range(n)]])
time = 0
while len(P) > 0:
    pi = P.popleft()
    if pi[1] > q:
        P.append([pi[0],pi[1]-q])
        time += q
    else:
        time += pi[1]
        print(pi[0],time)