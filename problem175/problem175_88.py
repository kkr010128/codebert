N = int(input())
S = input()
R = set()
G = set()
B = set()
for i, s in enumerate(S):
    if s == 'R':
        R.add(i)
    elif s == 'G':
        G.add(i)
    elif s == 'B':
        B.add(i)

ans = 0
for r in R:
    for g in G:
        ans += len(B)
        d = abs(r-g)
        if (r+g) % 2 == 0 and (r+g)//2 in B:
            ans -= 1
        if r+d in B or g+d in B:
            ans -= 1
        if r-d in B or g-d in B:
            ans -= 1
print(ans)
