def main():
    h,w,k=map(int,input().split())
    s=[list(input()) for _ in range(h)]
    
    ans=[[0]*w for _ in range(h)]
    for idx in range(h):
        if '#' in s[idx]:
            i=idx
            break
            
    start,j,cnt,first=i,0,1,True

    while i<h:
        if j==w:
            if first:
                ans[i]=ans[i-1]
                i+=1
                j=0
                continue
            first=True
            i+=1
            j=0
            cnt+=1
            continue

        if s[i][j]=='#':
            if first:
                first=False
                ans[i][j]=cnt
                j+=1
                continue
            cnt+=1
            ans[i][j]=cnt
        else:
            ans[i][j]=cnt

        j+=1
    
    for i in range(start):
        ans[i]=ans[start]
    
    for i in range(h):
        print(*ans[i]) 
    
if __name__=='__main__':
    main()