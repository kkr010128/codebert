# import math
N = int(input())

# Nが奇数の場合は-2していくと全て奇数になるので答えは0
# Nが偶数の場合を検討するべし
# Nが偶数の場合、明らかに2の倍数より5の倍数の方が少ないので5の倍数がいくつかで考える
if (N % 2 == 1):
    print(0)
    exit()

bunbo = 0
sum_5 = 0
while (10 * 5 ** bunbo) <= N:
    sum_5 += N // (10 * 5**bunbo)
    bunbo += 1

print(sum_5)
