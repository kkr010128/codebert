#coding:utf-8
#1_4_C 2015.3.29
while True:
    data = input().split()
    if data[1] == '?':
        break
    elif data[1] == '+':
        print(int(data[0]) + int(data[2]))
    elif data[1] == '-':
        print(int(data[0]) - int(data[2]))
    elif data[1] == '*':
       print(int(data[0]) * int(data[2]))
    elif data[1] == '/':
       print(int(data[0]) // int(data[2]))