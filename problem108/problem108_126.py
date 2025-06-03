#A - Payment
N = int(input())
#おつり
out = 1000 - (N % 1000)
if out == 1000: out = 0
# 出力
print(out)
