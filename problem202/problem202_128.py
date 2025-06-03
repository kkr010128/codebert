# 高橋くんが根性ありすぎるので, ループではTLE
# 単純に商と剰余の和と思いがちだが, そうでないことに注意
n, a, b = (int(x) for x in input().split())
if a == 0:
    print('0')
    exit()
count_a = n // (a + b)
leave = n % (a + b)
# 剰余がaを超えていた場合, aにする
if leave >= a: leave = a
ans = a * count_a + leave
print(ans)