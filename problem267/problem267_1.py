def I(): return int(input())
N = I()
S = input()
ans = 0
for i in range(1000):
    num = str(i).zfill(3)
    if S.find(num[0])==-1:
        continue
    S1 = S[S.find(num[0])+1:]
    if S1.find(num[1])==-1:
        continue
    S2 = S1[S1.find(num[1])+1:]
    if S2.find(num[2])==-1:
        continue
    ans += 1
print(ans)