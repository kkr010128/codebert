K, X = map(int,input().split())
price = 500
ans = "No"
if price*K >= X:
    ans = "Yes"
print(ans)
