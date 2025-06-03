from sys import stdin
from collections import deque
def main():
    #入力
    readline=stdin.readline
    k=int(readline())

    lunlun_number=[]
    d=deque(map(str,range(1,10)))
    cnt=0
    while cnt<k:
        now=d.popleft()
        lunlun_number.append(now)
        cnt+=1
        if now[-1]=="0":
            nex=("0","1")
        elif now[-1]=="9":
            nex=("8","9")
        else:
            last=int(now[-1])
            nex=(str(last-1),str(last),str(last+1))
        for x in nex:
            d.append(now+x)

    print(lunlun_number[k-1])

if __name__=="__main__":
    main()