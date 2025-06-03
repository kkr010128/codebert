# coding: utf-8

count = int(input())
num = input().rstrip().split(" ")

min,max = int(num[0]),int(num[0])
sum = 0

for i in range(count):
    sum = sum + int(num[i])
    if int(min) > int(num[i]):
        min = int(num[i])
    if int(max) < int(num[i]):
        max = int(num[i])

print(str(min) + " " + str(max) + " " + str(sum))