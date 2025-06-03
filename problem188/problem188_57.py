import heapq
x,y,a,b,c = map(int,input().split())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]
R = [-int(i) for i in input().split()]
P.sort(reverse=True)
P = P[:x]
Q.sort(reverse=True)
Q = Q[:y]
heapq.heapify(P)
heapq.heapify(Q)
heapq.heapify(R)
while R:
    if P[0] >= Q[0]:
        if Q[0] < -R[0]:
            heapq.heapreplace(Q, -heapq.heappop(R))
        else:
            break
    else:
        if P[0] < -R[0]:
            heapq.heapreplace(P,-heapq.heappop(R))
        else:
            break
print(sum(P)+sum(Q))