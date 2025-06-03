t=int(input())
taro=0
hanako=0
for i in range(t):
    S=input().split()

    if S[0]==S[1]:
        taro+=1
        hanako+=1
    elif S[0]>S[1]:
        taro+=3
    else:
        hanako+=3
print(taro,hanako)