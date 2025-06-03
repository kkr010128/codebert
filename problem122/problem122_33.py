N = int(input())
A = list(map(int,input().split()))
Q = int(input())
S = [list(map(int, input().split())) for l in range(Q)]

l = [0] * 10**6
tot = 0
for i in range(N) :
    l[A[i]]+=1
    tot += A[i]
for i in range(Q):
    s0 = S[i][0]
    s1 = S[i][1]
    tot += s1 * (l[s0] + l[s1]) - (s0 * l[s0] + s1*l[s1])
    l[s1] += l[s0]
    l[s0] = 0
    print(tot)