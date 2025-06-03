S = input()
S = S.replace('><','> <').split()

ans = 0
for i in S:
    j = max(i.count('>'),i.count('<'))
    k = min(i.count('>'),i.count('<'))-1
    for a in range(1,j+1):
        ans += a
    for b in range(1,k+1):
        ans += b

print(ans)