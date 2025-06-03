N, K, C = map(int, input().split())
S = input()

Sr = "".join(list(reversed(S)))

wd = []
wdl = []

pw = 0
pwl = 0

for d in range(K):

    # 先詰めを探す
    while True:
        if S[pw] == ('o'):
            wd.append(pw)
            break
        pw += 1
    pw += C + 1
    
    # 後詰めを探す
    while True:
        if Sr[pwl] == ('o'):
            wdl.append((N-1) - pwl)
            break
        pwl += 1
    pwl += C + 1

wdl.sort()
    
for i in range(K):
    if wd[i] == wdl[i]:
        print(wd[i] + 1)