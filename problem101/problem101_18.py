# coding:utf-8
a, b, c = map(int, input().split())
k = int(input())
counter = 0

while a >= b:
    counter += 1
    b = b * 2

while b >= c:
    counter += 1
    c = c * 2

if counter <= k:
    print('Yes')
else:
    print('No')
