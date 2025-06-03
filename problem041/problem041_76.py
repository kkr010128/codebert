#coding: UTF-8

def Circle(W,H,x,y,r):
    if x <= W - r and x >= r and y <= H-r and y >= r:
        return "Yes"
    else:
        return "No"

if __name__=="__main__":
    a = input().split(" ")
    ans = Circle(int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]))
    print(ans)