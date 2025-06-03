# coding: utf-8
# Here your code !

def test():
    line=input().rstrip()
    list=line.split(" ")
    try:
        a=int(list[0])
        b=int(list[1])
    except:
        print("input error")
        return -1 
    
    if(a>b):
        print("a > b")
    elif(a<b):
        print("a < b")
    elif(a==b):
        print("a == b")

test()