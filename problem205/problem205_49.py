N,P = map(int,input().split())
S = input()

if P in (2,5):
    ans = 0
    for i,c in enumerate(S):
        c = int(c)
        if c%P==0:
            ans += (i+1)
    print(ans)
else:
    ans = 0
    a = [0]
    j = 1
    for c in S[::-1]:
        c = int(c)
        a.append((a[-1] + j*c) % P)
        j *= 10
        j %= P
    from collections import Counter
    ctr = Counter(a)
    for k,v in ctr.items():
        ans += v*(v-1)//2
    print(ans)