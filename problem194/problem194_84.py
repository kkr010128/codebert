H,W=map(int,input().split())
S=[input() for _ in range(H)]
ans=float("inf")

counter=[[999]*W for _ in range(H)]

def search(i,j,count):
    global ans

    if counter[i][j]!=999:
        ans=min(ans,count+counter[i][j])
        return(counter[i][j])

    dist=999

    if i==H-1 and j==W-1:
        ans=min(ans,count)
        return 0
    countj=count
    counti=count
    
    if j<W-1:
        if S[i][j]=="." and S[i][j+1]=="#":
            countj+=1
        dist=search(i,j+1,countj) + (S[i][j]=="." and S[i][j+1]=="#")
    if i<H-1:
        if S[i][j]=="." and S[i+1][j]=="#":
            counti+=1
        dist=min(dist,search(i+1,j,counti)+(S[i][j]=="." and S[i+1][j]=="#"))
    
    counter[i][j]=dist
    return dist
search(0,0,(S[0][0]=="#")*1)
print(ans)