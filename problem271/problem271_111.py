n = int(input())
s = input()
ans = []

for i in range(len(s)):
    temp = ord(s[i]) +n
    if temp > 0x5a:
        temp -= 26
    ans.append(chr(temp))
    
for k in range(len(ans)):
    print(ans[k], end = "")