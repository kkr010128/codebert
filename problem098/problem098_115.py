n = int(input())
C = list(input())


W = C.count("W")
R = C.count("R")

# 仕切りより左側にある白石の数
w = 0
# 仕切りより右側にある赤石の数
r = R

ans = r

for i in range(n):
    if C[i] == "W":
        w += 1
    else:
        r -= 1
    ans = min(ans, max(w, r))
print(ans)