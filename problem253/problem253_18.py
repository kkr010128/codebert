n,a,b = map(int, input().split())
if a > b : a,b = b,a #swap
### 差が偶数
if (b-a)%2 == 0:
    print((b-a)//2)
if (b-a)%2 == 1:
    ### 1側で調整
    ichi = a + (b-a-1)//2
    ### n側で調整
    b = n-b
    a = n-a
    enu = b + 1 + (a-b-1)//2
    print(min(ichi,enu))