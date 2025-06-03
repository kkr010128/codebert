#coding: UTF-8

def Sort(a,b,c):
    box = 0
    if a > b:
        box = b
        b = a
        a = box
    if b > c:
        box = c
        c = b
        b = box
    if a > b:
        box = b
        b = a
        a = box
    return a,b,c

if __name__=="__main__":
    a = input().split(" ")
    a,b,c = Sort(int(a[0]),int(a[1]),int(a[2]))
    print(str(a)+" "+str(b)+" "+str(c))