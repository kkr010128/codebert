N=int(input())
Taro=0
Hanako=0
for i in range(N):
    T,H=map(str,input().split())
    if T<H:
        Hanako+=3
    elif H<T:
        Taro+=3
    else:
        Hanako+=1
        Taro+=1
print(Taro,Hanako)

