n = int(input())
a=list(map(int,input().split()))
 
kane=1000
kabu =0
 
for i in range(n-1):
    if a[i]<=a[i+1]:
        kabu+=kane//a[i]
        kane=kane%a[i]
    else:
        kane+=kabu*a[i]
        kabu=0

print(kane+kabu*a[n-1])