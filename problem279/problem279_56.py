n = int(input())
s = input()
x = n // 2
print(["Yes", "No"][n % 2 != 0 or s[:x] != s[x:]])