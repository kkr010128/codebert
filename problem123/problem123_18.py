n=int(input())
a=list(map(int,input().split()))

xor=0
for i in a:
    xor ^= i

pop=0 #xorのpopにする
while(xor >> pop >=1):
    pop += 1

sum_xor=xor #各猫の排他的論理和

ans=[]
for i in a:
    x=i^sum_xor
    ans.append(x)

print(" ".join(map(str, ans)))