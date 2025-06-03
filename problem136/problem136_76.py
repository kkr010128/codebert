n=int(input())

ans =0
for i in range(2,int(n**0.5)+5):
    cnt = 0
    while n%i==0:
        n//=i
        cnt += 1
    s=1
    while cnt-s>=0:
        cnt -= s
        s +=1
        ans += 1
if n!=1:ans+=1
print(ans)
