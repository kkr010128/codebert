def main():
    h,w,k=map(int,input().split())
    grid=[input() for _ in [0]*h]
    ans=[[0]*w for _ in [0]*h]
    berry=0
    for i in range(h):
        if "#" in grid[i]:
            cnt=0
            berry+=1
            for j in range(w):
                if grid[i][j]=="#":
                    cnt+=1
                    if cnt>1:
                        berry+=1
                ans[i][j]=berry
    for i in range(1,h):
        if ans[i][0]==0:
            for j in range(w):
                ans[i][j]=ans[i-1][j]
    for i in range(h-2,-1,-1):
        if ans[i][0]==0:
            for j in range(w):
                ans[i][j]=ans[i+1][j]         
    for i in ans:
        print(*i)
main()
