S = list(map(int, list(input())))[::-1]
N = len(S)
CNT = [0]*2019
CNT[0] = 1
num = 0
d = 0
for i in range(N):
    num += S[i]*pow(10, d, 2019)
    num %= 2019
    CNT[num] += 1
    d += 1
ans = 0 
for cnt in CNT:
    ans += (cnt*(cnt - 1)) // 2
print(ans)