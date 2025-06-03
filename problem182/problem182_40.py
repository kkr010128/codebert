N, K, C = map(int, input().split())
S = input().rstrip()
P = [0]*(N+1)
cl, l, cr, r = 0, 1, 0, 1
for i in range(N):
    if cl > C and S[i] != "x": cl = 0; l += 1
    cl += 1
    P[i+1] += l
    if cr > C and S[-1-i] != "x": cr = 0; r += 1
    cr += 1
    P[N-2-i] += r
for i in range(N):
    if P[i] < K and S[i] == "o":
        print(i+1)