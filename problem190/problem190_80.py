s = input()

flag = 1

l = len(s)

for i in range((l-1)//2):
    if s[i] == s[(l-1)//2 - 1-i]:
        continue
    else:
        flag = 0
        break

if s[:(l-1)//2] != s[(l+3)//2-1:]:
    flag = 0

print("Yes" if flag == 1 else "No")
