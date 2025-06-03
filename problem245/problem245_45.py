# 各桁の数値の総和を計算する.
def calc_digit_sum(num):
    sums = 0
    while num > 0:
        sums += num % 10
        num //= 10
    return sums


n = int(input())
s = input()

cnt = 0
for index in range(n-2):
    if s[index:index+3] == "ABC":
        cnt += 1
print(cnt)