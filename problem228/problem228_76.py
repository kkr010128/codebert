H = int(input())
ans = 0
attack_cnt = 0
while H > 0:
    ans += 2 ** attack_cnt
    attack_cnt += 1
    H //= 2

print(ans)