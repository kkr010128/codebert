from sys import stdin
def main():
    #入力
    readline=stdin.readline
    h,w,k=map(int,readline().split())
    grid=[readline().strip() for _ in range(h)]

    ans=float("inf")
    for i in range(1<<(h-1)):
        div=[(i>>j)&1 for j in range(h-1)]
        l=len([0 for i in range(h-1) if div[i]])+1
        cnt=[0]*l
        tmp=0
        for j in range(w):
            now=0
            flag=False
            for i_2 in range(h):
                if grid[i_2][j]=="1":
                    cnt[now]+=1
                    if cnt[now]>k:
                        flag=True
                        break
                if i_2<h-1 and div[i_2]==1: now+=1
            if flag:
                tmp+=1
                cnt=[0]*l
                now=0
                flag=False
                for i_2 in range(h):
                    if grid[i_2][j]=="1":
                        cnt[now]+=1
                        if cnt[now]>k:
                            flag=True
                            break
                    if i_2<h-1 and div[i_2]==1: now+=1
                if flag: break
        else:
            tmp+=l-1
            ans=min(ans,tmp)

    print(ans)

if __name__=="__main__":
    main()