from collections import defaultdict
N, P = map(int,input().split())
S = input()

if P==5:
    ans = 0
    for i,m in enumerate(S):
        if m == '5' or m == '0':
            ans += i+1
elif P==2:
    ans = 0
    for i,m in enumerate(S):
        if int(m) % 2 ==0:
            ans += i+1
else:
    S = S[::-1]
    primdic = defaultdict(int)
    before = 0
    for i in range(0,N):
        now = (int(S[i])*pow(10,i,P)+before)%P
        primdic[now] += 1
        before = now
    # 文字なしの時はあまり0なので
    primdic[0] += 1
    ans = 0
    for value in primdic.values():
        ans += value*(value-1)//2
print(ans)