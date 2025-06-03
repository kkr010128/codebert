S = input()
K = int(input())

N = len(S)
#全て同じ文字の時
if len(set(S)) == 1:
    print(N*K//2)
    exit()

#隣合う文字列が何個等しいか
cycle = 0
tmp = S[0]
cnt = 1
for i in range(1, N):
    if tmp != S[i]:
        cycle += cnt//2
        tmp = S[i]
        cnt = 1
    else:
        cnt += 1
cycle += cnt//2

if S[0] == S[-1]:
    i = 0
    a = 0
    tmp = S[0]
    while S[i] == tmp:
        i += 1
        a += 1
    j = N-1
    b = 0
    tmp = S[-1]
    while S[j] == tmp:
        j -= 1
        b += 1
    print((cycle*K) - (a//2 + b//2 - (a+b)//2)*(K-1))
else:
    print(cycle*K)