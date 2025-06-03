# coding: utf-8
# Your code here!

n = int(input())
m = [1,1]
if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    for i in range(2, n+1):
        m.append( m[i-1] + m[i-2] )
    print(m.pop())
