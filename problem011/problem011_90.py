#coding:UTF-8
def GCD(x,y):
    d=0
    if x < y:
        d=y
        y=x
        x=d
    if y==0:
        print(x)
    else:
        GCD(y,x%y)
if __name__=="__main__":
    a=input()
    x=int(a.split(" ")[0])
    y=int(a.split(" ")[1])
    GCD(x,y)