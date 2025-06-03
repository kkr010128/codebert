# coding: utf-8

n = int(input().rstrip())
count = 0

for i in range(1,n//2+1):
    m = n - i
    if i != m:
        count += 1
    
print(count)