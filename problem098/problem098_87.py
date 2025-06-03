N = int(input())
c = list(input())

#cを[R,R,R,.....,R,W,W,W,.....,W]の形にする。

div = c.count('R')

c_for = c[:div]
c_lat = c[div:]

ans = 0

replace = min(c_for.count('W'), c_lat.count('R'))
change = max(c_for.count('W'), c_lat.count('R')) - replace

ans = replace + change
#実質 ans = max(c_for.count('W'), c_lat.count('R')) やんけ！

print(ans)