N,A,B = map(int,input().split())
balls = A + B
N_surplus = N%balls
if N_surplus < A:
    blues = (N//balls)*A + N_surplus
else:
    blues = (N//balls)*A + A
print(blues)