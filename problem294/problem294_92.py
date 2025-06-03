N=int(input())
L=list(map(int,input().split()))
sort_L=sorted(L,reverse=True)
ans=0
for n in range(N-2):
    for o in range(n+1,N-1):
        lar=sort_L[n]
        kouho=sort_L[o+1:]
        mid=sort_L[o]
        sa=lar-mid
        left=0
        right=N-o-2
        if kouho[-1]>sa:
            ans+=right+1
        else:
            while right > left + 1:
                half = (right + left) // 2
                if kouho[half] <= sa:
                    right = half
                else:
                    left = half
            if kouho[right]<=sa and kouho[left]<=sa:
                continue
            elif kouho[right]>sa:
                ans+=right+1
            else:
                ans+=left+1
print(ans)
