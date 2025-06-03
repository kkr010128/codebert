import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()
n = int(input())
# n,m = map(int, input().split())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]


xl=[]
for i in range(n):
    x,l = map(int, input().split())
    xl.append((x,l))


def main():
    p = []
    for x,l in xl:
        p.append([x-l,x+l])
    p = sorted(p, key=lambda x:x[1])

    ans = 0
    mx = -10**10
    for st in p:
        s,t = st[0],st[1]
        if s>=mx:
            ans+=1
            mx=t
    print(ans)



    
    

if __name__ == '__main__':
    main()