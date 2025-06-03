#coding:utf-8
#1_4_C 2015.3.29
while True:
    data = input()
    if '?' in data:
        break
    print(eval(data.replace('/','//')))