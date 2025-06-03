N=int(input())
ans=[]
for i in range(1,99):
    if N>26**i:
        N-=26**i
    else:
        N-=1
        for l in range(i):
            key=(chr(ord("a")+(N%26)))
            N=int(N/26)
            ans.append(key)
        break
    
ans.reverse()
for i in range(len(ans)):
    print(ans[i],end="")