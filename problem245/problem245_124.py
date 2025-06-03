n = int(input())
s = input()
ans = 0
for i in range(n - 2):
    a = s[i:i + 3]
    if a == "ABC":
        ans += 1
print(ans)