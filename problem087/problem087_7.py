n = list(input())
tmp = 0
for i in n:
    tmp += int(i) % 9
ans = "Yes" if tmp % 9 == 0 else "No"
print(ans)
