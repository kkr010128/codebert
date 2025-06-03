n=int(input())

taro=0
hanako=0

for i in range(n):
    T,H=map(str,input().split())
    if T<H:
        hanako+=3
    elif T>H:
        taro+=3
    else:
        taro+=1
        hanako+=1

print(taro, hanako)

