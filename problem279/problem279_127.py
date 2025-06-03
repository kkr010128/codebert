# 145 B

n = int(input())
s = input()

if len(s) % 2 == 0:
    x = len(s) // 2

    if s[:x] == s[x:]:
        print("Yes")
    else:
        print("No")
else:
    print("No")