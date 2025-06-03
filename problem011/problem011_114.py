#16D8101012J 伊藤惇 dj Python3 

def Greatest_Common_Divisor(x,y):
    if y>x:
        x,y=y,x
    if x>=y and y>0:
        return Greatest_Common_Divisor(y,x%y)
    return x

if __name__ == "__main__":
    x=list(map(int,input().split()))
    print(Greatest_Common_Divisor(x[0],x[1]))


