#coding: UTF-8
import math

def RN(n,a):
    ans=""
    for i in range(int(n)):
        ans+=a[int(n)-1-i]+" "
    print(ans[:-1])

if __name__=="__main__":
    n=input()
    a=input()
    List=a.split(" ")
    RN(n,List)