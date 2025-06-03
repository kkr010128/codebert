#!/usr/bin python3
# -*- coding: utf-8 -*-

def pc(x):
    return format(x, 'b').count('1')

N = int(input())
X = input()
Xn = int(X,2)
p = pc(Xn)
X = list(X)

Xp = Xn%(p+1)
if p==1:
    Xm = 0
else:
    Xm = Xn%(p-1)

def f(i):
    if p==1 and X[i]=='1':
        #Xi == 0 > POPcount ==0
        return 0
    else:
        if X[i]=='1':
            # p->p-1
            ret = Xm - pow(2, N-1-i, p-1)
            ret %= p-1
        else:
            # p->p+1
            ret = Xp + pow(2, N-1-i, p+1)
            ret %= p+1
        cnt = 1
        while ret > 0:
            ret %= pc(ret)
            cnt += 1
        return cnt

def main():
    for i in range(N):
        ret = f(i)
        print(ret)

if __name__ == '__main__':
    main()
