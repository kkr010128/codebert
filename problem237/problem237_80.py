def main():
    import sys
    input=sys.stdin.readline
    n=int(input())
    lst=[]
    for i in range(n):
        a,b=map(int,input().split())
        lst.append([a-b,a+b])
    lst=sorted(lst,key=lambda x:x[1])
    ans=0
    end=-float("inf")
    for i in lst:
        if i[0]>=end:
            ans+=1
            end=i[1]
    print(ans)
if __name__=="__main__":
    main()