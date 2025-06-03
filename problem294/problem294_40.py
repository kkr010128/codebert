N=int(input())
L= list(map(int,input().split()))
L_sorted=sorted(L,reverse=False)#昇順
count=0
for i in range(N):
    for j in range(i+1,N):
        a=L_sorted[i]
        b=L_sorted[j]
        n=a+b
        fin=N
        sta=0
        while sta+1<fin:
            m=((fin-sta)//2)+sta
            if L_sorted[m]<n:
                sta=m       
            else:
                fin=m   
        count+=sta-j
print(count)