n = int(input())
a = list(map(int, input().split()))
ans = [0]*n

for boss in a:
    ans[boss-1] += 1
    
for sub in ans:
    print(sub)