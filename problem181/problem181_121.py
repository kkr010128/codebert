#

import sys
input=sys.stdin.readline

def main():
    K=int(input())
    lunlun=[1,2,3,4,5,6,7,8,9]
    ind=0
    lll=9
    for dig in range(12):
        l=lll
        for i in lunlun[ind:]:
            s=str(i)
            x=int(s[dig])
            if 0<=x-1<=9:
                lunlun+=[int(s+str(x-1))]
                lll+=1
            if 0<=x<=9:
                lunlun+=[int(s+str(x))]
                lll+=1
            if 0<=x+1<=9:
                lunlun+=[int(s+str(x+1))]
                lll+=1
            if lll>K:
                break
        ind=l
    lunlun.sort()
    print(lunlun[K-1])
    
    
if __name__=="__main__":
    main()
