a = 0
for c in map(int, input()):
    a += c
print("Yes" if a % 9 == 0 else "No")