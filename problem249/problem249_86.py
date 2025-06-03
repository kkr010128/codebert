# ABC149
# B Greesy Takahashi
# takはA枚、aokiはB枚、TAKはK回
a, b, k = map(int, input().split())
if k > a:
    if k - a > b:
        print(0,0)
    else:
        print(0,b - (k - a))
else:
    print(a-k,b)
