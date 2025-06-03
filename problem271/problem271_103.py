# 与えられた数値の桁数と桁値の総和を計算する.
def calc_digit_sum(num):
    digits = sums = 0
    while num > 0:
        digits += 1
        sums += num % 10
        num //= 10
    return digits, sums


n = int(input())
s = [((ord(ch) - 65 + n) % 26) + 65 for ch in input()]
print("".join(map(chr, s)))