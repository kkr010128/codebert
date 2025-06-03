# import itertools
S = input()[::-1]
# l = len(S)
# nums = range(1, l+1)
count = [0]*2019
count[0] = 1
num = 0
d = 1
for i in S:
    num += int(i)*d
    num %= 2019
    count[num] += 1
    d *= 10
    d %= 2019

ans = 0
for i in count:
    ans += i*(i-1)//2
print(ans)
