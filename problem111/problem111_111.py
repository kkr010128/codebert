N=int(input())
a=list(map(int, input().split()))
 
a=sorted(a)[::-1] 
ans =a[0]

if len(a)%2 !=0:
    for i in range(1,int((len(a))/2)+1):
        for j in range(2):
            ans +=a[i]
    print(ans-a[int((len(a))/2)])
else:
    for i in range(1,(len(a))//2):
        for j in range(2):
            ans +=a[i]
    print(ans)