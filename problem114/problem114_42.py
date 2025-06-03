import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
D = int(readline())
C = list(map(int,readline().split()))
score = []
for i in range(D):
    s = list(map(int,readline().split()))
    score.append(s)
t = list(map(int,read().split()))
last = [0] * 26
S = 0
for d in range(D):
    select = t[d]-1
    S += score[d][select]
    last[select] = d+1
    for i in range(26):
        S -= C[i] * (d+1-last[i]) 
    print(S)