n = int(input())
s = str(input())
if n % 2 == 1:
    print("No")
    exit()
if s[:n // 2] == s[n // 2:]:
    print("Yes")
    exit()
print("No")