# 2020/08/16
# AtCoder Beginner Contest 030 - A

# Input
h = int(input())
w = int(input())
n = int(input())

# Calc
ans = n // max(h, w)
if n % max(h, w) > 0:
    ans = ans + 1

# Output
print(ans)
