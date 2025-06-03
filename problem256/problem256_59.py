aa, bb = map(int,input().split())

a = aa
b = bb
r = 0
# 最大公約数を求める
while 1:
    a, b = max(a,b), min(a,b)
    a = a % b
    if a == 0:
        r = b
        break

print(aa//r*bb)
