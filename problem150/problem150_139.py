N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A
#print(A)

machi = 1
road = [0,1]
Keiyu = [0]*(N+1)

for n in range(1, N+1):
    if Keiyu[machi] == 0:
        Keiyu[machi] = n
        road.append(A[machi])
        machi = A[machi]
    else:
        S = Keiyu[machi] - 1
        E = n - 1
        break

#print(road)
#print(Keiyu)
#print(S)
#print(E)

if K <= S:
    print(road[K+1])
else:
    K = K - S
    K = S + K % (E-S)
    print(road[K+1])

