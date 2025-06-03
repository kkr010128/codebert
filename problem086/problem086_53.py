# coding: utf-8
# Your code here!
[n,x,t] = input().split()
n = int(n)
x = int(x)
t = int(t)

i = 1
while True:
    if i*x >= n:
        break
    i += 1
    
print(i*t)