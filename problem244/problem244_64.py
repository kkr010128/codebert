# 500 Yen Coins
K, X = map(int, input().split())

if K * 500 >= X:
    ans = 'Yes'
else:
    ans = 'No'    

print(ans)