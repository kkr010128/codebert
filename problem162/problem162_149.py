from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,M=map(int,readline().split())
    a=1
    b=N-1
    if N%2==1:
        for _ in range(M):
            print(a,b)
            a+=1
            b-=1
    else:
        flag=False
        for _ in range(M):
            if flag==False and b-a<=N//2:
                flag=True
                b-=1
                print(a,b)
                a+=1
                b-=1
            else:
                print(a,b)
                a+=1
                b-=1

if __name__=="__main__":
    main()