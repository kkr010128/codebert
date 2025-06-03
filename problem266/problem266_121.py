DP = [False]*100001
DP[0] = True
for TN in range(0,100001):
    if TN>=100 and DP[TN-100]:
        DP[TN] = True
        continue
    if TN>=101 and DP[TN-101]:
        DP[TN] = True
        continue
    if TN>=102 and DP[TN-102]:
        DP[TN] = True
        continue
    if TN>=103 and DP[TN-103]:
        DP[TN] = True
        continue
    if TN>=104 and DP[TN-104]:
        DP[TN] = True
        continue
    if TN>=105 and DP[TN-105]:
        DP[TN] = True
        continue
print([0,1][DP[int(input())]])