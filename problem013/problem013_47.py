N = input()
R = [int(raw_input()) for _ in xrange(N)]
S = [0 for i in xrange(N)]
S[N-1] = R[N-1]
for i in xrange(N-2, -1, -1):
    S[i] = max(R[i], S[i+1])
ans = float('-inf')
for i in xrange(N-1):
    ans = max(ans, S[i+1]-R[i])
print ans