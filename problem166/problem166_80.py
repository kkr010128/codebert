from collections import deque
s=input()[::-1]
l=[0]*2019
ten=1
sm=0
cnt=0
l[0]=1
for i in range(len(s)):
    sm += int(s[i])*ten
    sm %= 2019
    cnt += l[sm]
    l[sm] += 1
    ten = ten *10 %2019
print(cnt)