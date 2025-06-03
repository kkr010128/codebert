
#1,2,3,4,5,6,7,8,9
#10,11,12,21,22,23,32,33,34,43,44,45,54,55,56,....,98,99
#100,101,110,111,112,121,122,123
#210,211,212,221,222,223,232,233,234
#321,322,323,332,333,334,343,344,345
#1000,1001,1010,1011,1012,

from collections import deque

def main():
    K=int(input())

    lnln=deque([i for i in range(1,10)])

    for _ in range(K):
        n=lnln.popleft()
        if n%10!=0:
            lnln.append(n*10+(n%10)-1)
        lnln.append(n*10+(n%10))
        if n%10!=9:
            lnln.append(n*10+(n%10)+1)

    print(n)

if __name__=="__main__":
    main()
