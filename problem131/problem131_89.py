a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = int(input())
diff = (a[1]-b[1])*t # 1秒ごとに縮まる
adiff = abs(a[0]-b[0]) # 元々の差
if diff >= adiff:
  print('YES')
else:
  print('NO')