# -*- coding:utf-8 -*-

def gcd(a,b):
    big,small=max(a,b),min(a,b)
    while big%small!=0:
        big,small=small,big%small
    return small

def lcm(a,b):
    return int(a*b/gcd(a,b))
 
def main():
    while True:
        try:
            IN=input()
            val=IN.split()
            g=gcd(int(val[0]),int(val[1]))
            l=lcm(int(val[0]),int(val[1]))

            print(g,l)
        except:
            break
if __name__ == '__main__':
    main()