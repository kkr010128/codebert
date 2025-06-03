s = input()
k = int(input())
ans = 0
soui = 0
moji = s[0]

for i in range(1,len(s)):
    if s[i] == s[i-1] and soui == 0:
        ans += 1
        soui = 1
    elif soui == 1:
        soui = 0


flag = 0
a = 0
b = 0

while s[0] == s[a] and a != len(s)-1:
    a += 1

while s[len(s)-1-b] == s[len(s)-1] and b != len(s)-1:
    b += 1


if s[0] == s[len(s)-1]:
    flag = 1

for i in range(len(s)):
    if moji != s[i]:
        break
    elif i == len(s)-1:
        flag = 2

if flag == 1:
    print((k*ans)-((k-1)*((a//2)+(b//2)-((a+b)//2))))
elif flag == 2:
    print((k*len(s))//2)
else:
    print(k*ans)
