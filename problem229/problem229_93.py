h,n,*t = map(int,open(0).read().split())

dp = [0] + [10**8]* h

for a,b in  zip(*[iter(t)]*2):
    for life_point in range(h +1):
        
        original_life = max(0,life_point - a)
#         print(original_life)
        magic_consum = dp[original_life]+ b
#         print(magic_consum)
        dp[life_point] = min(dp[life_point],magic_consum)
#         print(dp)
print(dp[h])