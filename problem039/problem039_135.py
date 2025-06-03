# coding: utf-8
data = input()
data = list(map(int,data.split(" ")))

if data[0] < data[1]:
    if data[1] < data[2]:
        print("Yes")
    else:
        print("No")
else:
    print("No")