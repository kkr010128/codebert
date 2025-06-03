n = int(input())

s=""
keta=0
n-=1
while 1 :
    c = n%26
    s=chr( 97+c )+s
    if n//26>0 :
        n=n//26
        n-=1
        keta+=1
    else:
        break

print(s)
