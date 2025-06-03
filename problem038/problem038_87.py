#coding: UTF-8

def SLE(a,b):
    if a > b:
        return "a > b"
    elif a < b:
        return "a < b"
    else:
        return "a == b"

if __name__=="__main__":
    a = input().split(" ")
    ans = SLE(int(a[0]),int(a[1]))
    print(ans)