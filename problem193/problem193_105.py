h,w,k = map(int,input().split())
s = [list(map(int,input())) for _ in range(h)]
    
ans = h*w
for div in range(1<<(h-1)):
    row = 0
    S = [[0]*w]
    S[row] = [s[0][i] for i in range(w)]
    for i in range(1,h):
        if 1&(div>>i-1):
            row += 1
            S.append([s[i][j] for j in range(w)])
        else:
            S[row] = [S[row][j]+s[i][j] for j in range(w)]
            
    count = [0]*(row+1)
    ans_ = row
    a = True
    for i in range(w):
        for j in range(row+1):
            if S[j][i] > k:
                a = False
                break
            count[j] += S[j][i]
            if count[j] > k:
                ans_+=1
                count = [0]*(row+1)
                for l in range(row+1):
                    count[l] += S[l][i]
                break
        if ans_ >= ans or a==False:
            break
    
    if a:
        ans = min(ans,ans_)

print(ans)