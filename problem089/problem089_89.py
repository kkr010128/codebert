H, W, M = map(int, input().split())
R = [0]*H #各行にある爆弾の個数
C = [0]*W #各列にある爆弾の個数
bombs = []
for _ in range(M):
    h, w = map(lambda x: int(x)-1, input().split())
    R[h] += 1
    C[w] += 1
    bombs.append((h, w))

R_max = max(R)
C_max = max(C)

### Rが最大かつCが最大な座標であって、
# そこに爆弾がない場合があれば
# 答えがR_max+C_max
# なければR_max+C_max-1
count = 0 # 爆弾がある座標であって、Rが最大かつCが最大の組の個数
for bx, by in bombs:
    if R[bx] == R_max and C[by] == C_max:
        count += 1

count_R = R.count(R_max)
count_C = C.count(C_max)
if count >= count_R*count_C:
    ans = R_max + C_max - 1
else:
    ans = R_max + C_max
print(ans)