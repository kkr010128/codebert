a=list(map(int, input().split(' ')))
# 起きてる時間（分）の計算
h=a[2]-a[0]
m=a[3]-a[1]
mt=h*60+m
# 時間の表示
print(mt-a[4])