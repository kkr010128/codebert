n = input()
ans = 0
for nn in n:
    ans += int(nn)
print('Yes') if ans%9 == 0 else print('No')