ans = 0
for a in range(1, int(input())+1):
    if a % 3 != 0 and a % 5 != 0:
        ans += a
print(ans)