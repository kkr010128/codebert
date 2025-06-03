#coding:utf-8

m = 0
f = 0
r = 0

while m + f + r >-3:
    m , f, r =[int(i) for i in input().rstrip().split(" ")]
    if m+f+r == -3:
        break
    
    if m == -1:
        print("F")
    elif f == -1:
        print("F")
    elif m+f <30:
        print("F")
    elif m+f <50:
        if r>=50:
            print("C")
        else:
            print("D")
    elif m+f <65:
        print("C")
    elif m+f <80:
        print("B")
    else:
        print("A")