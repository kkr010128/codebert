n = int(raw_input())
A = map(int, raw_input().strip().split(' '))
q = int(raw_input())
M = map(int, raw_input().strip().split(' '))


S = [0]*len(A)
flags = [False]*len(M)
def brute_force(n):
    if n == len(S):
        ans = 0
        for i in range(len(S)):
            if S[i] == 1: ans += A[i]
        for i in range(len(M)):
            if ans == M[i]: flags[i] = True
    else:
        S[n] = 0
        brute_force(n+1)
        S[n] = 1
        brute_force(n+1)


brute_force(0)

for flag in flags:
    if flag: print "yes"
    else: print "no"