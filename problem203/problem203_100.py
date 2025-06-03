a,b = map(int,input().split())
# 8% -> [a,a+1)
# 10% -> [b,b+1)
# max(a*100/8, b*10) <= 元の価格 < min((a+1)*100/8, (b+1)*10)
min8 = a*(100/8)
max8 = (a+1)*(100/8)
min10 = b*10
max10 = (b+1)*10
mi = int(max(min8, min10) - 0.001) + 1
ma = int(min(max8, max10) - 0.001)
if mi > ma:
    ans = -1
else:
    ans = mi
print(ans)