import sys
(a, b ,c) = [int(i) for i in input().split(' ')]
x = a
cnt = 0
while x <= b:
    if (c % x == 0) : cnt+=1
    x += 1
else:        
    print(cnt)