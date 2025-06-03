n = input()
t = len(n)+1
dp1 = [0] * t
dp2 = [0]*t
dp2[0] = 1

for i in range(t-1):
    x = int(n[i])
    dp1[i + 1] = min(dp1[i] + x, dp2[i] + 10 - x)
    x += 1
    dp2[i+1] = min(dp1[i]+x, dp2[i]+10-x)
print(dp1[-1])