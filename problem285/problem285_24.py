import sys
import math
import itertools as it
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    s = S()
    n = len(s)+1
    a = [0]*n
    for i in range(n-1):
        if s[i] == "<":
            a[i+1] = max(a[i+1],a[i]+1)
    for i in range(n-2,-1,-1):
        if s[i] == ">":
            a[i] = max(a[i],a[i+1]+1)
    print(sum(a))