S = input()
 
# 高々2^3=8通りなので、全て列挙すればよい
# RRR RRS SRR RSR RSS SRS SSR SSS
ans = 0
if S == 'RRR': ans = 3
elif S == 'SRR' or S == 'RRS': ans = 2
elif S == 'SSS': ans = 0
else: ans = 1
  
print(ans)