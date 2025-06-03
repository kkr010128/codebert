N = int(input())

if N == 1:
    print(0)
    exit()

if N == 2:
    print(2)
    exit()

# N >= 3

# 全事象
all_pattern = 10 ** N

# 0も9もない
pattern_a = 8 ** N

# 0あるが9ない
pattern_b = 9 ** N - 8 ** N

ans = all_pattern - pattern_a - pattern_b * 2
ans = ans % (10**9 + 7)

print(ans)