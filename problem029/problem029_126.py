#-*-coding:utf-8-*-

from decimal import Decimal
import math

def main():
    x1,y1,x2,y2 = map(Decimal,input().split())
    print("{:.8f}".format(math.sqrt((x2-x1)**2+(y2-y1)**2)))

if __name__=="__main__":
    main()
