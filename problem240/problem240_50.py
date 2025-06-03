N, M = map(int, input().split())
p = [0] * M
S = ['a'] * M
for i in range(M):
    p[i], S[i] = input().split()
    p[i] = int(p[i])

ansac = pen = 0
answa = [0] * N
flg = [0] * N

for i in range(M):
    if flg[p[i]-1] == 1:
        continue
    if S[i] == 'WA':
        answa[p[i]-1] += 1
    elif S[i] == 'AC':
        ansac += 1
        pen += answa[p[i]-1]
        flg[p[i]-1] = 1

print(ansac, pen)