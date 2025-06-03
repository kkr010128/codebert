# coding: utf-8

num = int(input())
number = input().split()
count, count2 = 0, 0
table = list(number)
for i in number:
    if int(i) % 2 == 0:
        count += 1
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            count2 += 1

if count == count2:
    print("APPROVED")
else:
    print("DENIED")