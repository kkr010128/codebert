n=int(input())
a=list(map(int,input().split()))
money=1000
kabu=0
for i in range(n-1):
    if a[i]<a[i+1] and a[i]<=money:
        kabu+=money//a[i]
        money-=kabu*a[i]
    if a[i]>a[i+1] and kabu>0:
        money+=kabu*a[i]
        kabu=0
if kabu>0:
    money+=kabu*a[-1]
print(money)
