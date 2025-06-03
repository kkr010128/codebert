#-*-coding:utf-8-*-

import sys

def main():
    n = int(input())
    ans=0
    b=0

    for a in range(1,n):
        #A*B+C=n → A <= n-c//b
        #cは1<=c<=nなのでbで可変
        b=(n-1)//a
        ans+=b
    print(ans)


if __name__ == "__main__":
    main()