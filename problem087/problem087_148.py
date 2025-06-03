n = list(input())

ans = 0
for i in n:
    ans += int(i)
    ans = ans%9

print('Yes' if ans == 0 else 'No')