nn = [0] + list(map(int, list(input())))
dp0, dp1 = 0, 0
for i in range(len(nn)):
	dp0, dp1 = nn[i] + min(dp1, dp0), 9 - nn[i] + min(dp1, dp0 + 2)
print(min(dp0, dp1))