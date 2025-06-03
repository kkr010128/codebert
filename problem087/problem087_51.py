n = input()
res = 0
for i in range(len(n)):
    res += int(n[i])
print("Yes" if res%9 == 0 else "No")