n = int(input())
s = input()
ans = ''
for i in s:
    next_number = ord(i)+n
    if next_number > 90:
        next_number -= 26
        ans += chr(next_number)
    else:
        ans += chr(next_number)
print(ans)    