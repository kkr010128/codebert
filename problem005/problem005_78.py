import sys
def GcdLCM():
    for line in sys.stdin:
        x,y=map(int,line.split())
        if x==None:
            break
        
        gcd = Gcd(x,y)
        lcm = int(x*y/gcd)

        print("{} {}".format(gcd,lcm))
       
def Gcd(x,y):
    while x!=0:
        x,y=y%x,x
    return y
        
    
GcdLCM()