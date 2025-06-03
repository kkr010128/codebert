n = int(input())
a = list(map(int,input().split()))

l = sum(a)
half = 0
tmp=a[0]
while tmp<l/2:
    half+=1
    tmp+=a[half]
    
    
print(int(min(tmp-l/2,abs(tmp-a[half]-l/2))*2))