#coding:utf-8
x=""
while x != "0":
    x = input().rstrip()

    if x =="0":
        break
    
    y = sum(list(map(int , list(x))))
    print(y)