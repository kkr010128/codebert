import sys, math
from collections import defaultdict
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7

def main():
    n = int(input())
    dic = defaultdict(int)
    dic1 = defaultdict(int)
    for _ in range(n):
        a,b = map(int,input().split())
        if a != 0 and b == 0:
            a = 1
        elif a == 0 and b != 0:
            b = 1
        else:
            if not (a==0 and b==0):
                m = gcd(a,b)
                a //= m
                b //= m
        if a < 0 and b < 0:
            a = -a
            b = -b
        if a < 0 and b > 0:
            a = -a
            b = -b
        index = ' '.join([str(a),str(b)])
        dic[index] += 1
        dic1[index] += 1
    ans = 1
    dic2 = defaultdict(int)
    for e in dic:
        a,b = map(int,e.split())
        if a == 0 and b == 0:
            continue
        flag = 0
        if a == 0 and b == 1:
            rev = ' '.join([str(1),str(0)])
        elif a == 1 and b == 0:
            rev = ' '.join([str(0),str(1)])
        elif a > 0 and b > 0:
            rev = ' '.join([str(b),str(-a)])
        else:
            rev = ' '.join([str(-b),str(a)])
        if dic1[rev] > 0 and dic2[rev] == 0:
            dic2[rev] = 1
            dic2[e] = 1
            flag = 1
        if flag:
            continue
        n1 = pow(2,dic[e],mod)
        n2 = pow(2,dic1[rev],mod)
        ans *= (n1+n2-1)
        ans %= mod
    print((ans-1+dic['0 0'])%mod)
    
if __name__ == "__main__":
    main()