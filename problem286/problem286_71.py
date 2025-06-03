# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


a, b = map(int, input().split())
if 1 <= a <= 9 and 1 <= b <= 9:
    print(a * b)
    exit()
print(-1)