#coding:utf-8
#1_6_A 2015.4.1
n = int(input())
numbers = list(map(int,input().split()))

for i in range(n):
    if i == n - 1:
        print(numbers[-i-1])
    else:
        print(numbers[-i-1], end = ' ')