import sys

N = int(sys.stdin.readline().strip())

S = []
for _ in range(N):
    s_i = sys.stdin.readline().strip()
    S.append(s_i)

# left bracket - right bracketを高さとした、最小の高さと最終的な高さの座標列
# ex)
# ")": (-1, -1)
# "(": (1, 1)
# "()": (1, 0)
# ")()(": (-1, 0)
# "))))(((((: (-4, 1)

plus_seqs = []
minus_seqs = []
for s_i in S:
    h = 0
    min_h = float("inf") 
    for bracket in s_i:
        if bracket == "(":
            h += 1
        else:
            h -= 1
        min_h = min(min_h, h)
            
    if h >= 0:
        plus_seqs.append((min_h, h))
    else:
        # minus_seqs.append((-1 * min_h, -1 * h))
        minus_seqs.append((min_h - h, -1 * h))

# print(plus_seqs)
# print(minus_seqs)

hight = 0
for (min_h, h) in sorted(plus_seqs, reverse=True):
    if hight + min_h < 0:
        print("No")
        sys.exit()
    hight += h

hight2 = 0
for (min_h, h) in sorted(minus_seqs, reverse=True):
    if hight2 + min_h < 0:
        print("No")
        sys.exit()
    hight2 += h

# print(hight, hight2)
if hight == hight2:
    print("Yes")
else:
    print("No")