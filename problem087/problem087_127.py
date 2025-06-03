n = input()
m = len(n)
x = 0
for i in range(m):
    x += int(n[i])
print("Yes" if x % 9 == 0 else "No")