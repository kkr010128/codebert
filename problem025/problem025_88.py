def search(l, m):
    #dp = [[None for _ in range(len(l) + 1)] for __ in range(m + 1)]
    dp = [[False for _ in range(m+1)] for __ in range(len(l) + 1)]
    dp[0][0]= True
    for i in range(len(l)):
        for mi in range(m + 1):
            if l[i] <= mi:
                dp[i+1][mi] = dp[i][mi - l[i]] or dp[i][mi]
            else:
                dp[i+1][mi] = dp[i][mi]
    return dp[len(l)][m]


n = int(input())
l = list(map(int, input().split()))
q = int(input())
ms = list(map(int, input().split()))

for m in ms:
    if search(l, m):
        print('yes')
    else:
        print('no')

