import sys
A,V = map(int, input().split())
B,W = map(int, input().split())
T = int(input())

#これO(1)で解けそう。

# スピードが同じ or 逃げる方のスピードが速いと無理
if V <= W:
    print("NO")
    sys.exit()



# 鬼の方がスピードが速い場合で場合訳
distance_AB = abs(A-B)
speed_AB = abs(V-W)

if speed_AB * T >= distance_AB:
    print("YES")
else:
    print("NO")