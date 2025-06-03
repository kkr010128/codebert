S = input()
K = int(input())

ss = []
seq = 1
for a,b in zip(S,S[1:]):
    if a==b:
        seq += 1
    else:
        ss.append(seq)
        seq = 1
ss.append(seq)

if len(ss)==1:
    print(len(S)*K//2)
    exit()

if S[0] != S[-1]:
    ans = sum([v//2 for v in ss]) * K
    print(ans)
else:
    ans = sum([v//2 for v in ss[1:-1]]) * K
    ans += (ss[0]+ss[-1])//2 * (K-1)
    ans += ss[0]//2 + ss[-1]//2
    print(ans)