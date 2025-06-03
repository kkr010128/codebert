k = int(input())
a, b = map(int,input().split())

flg = False
for i in range(a, b+1):
    if i % k == 0:
        flg = True
        break
print('OK') if flg else print('NG')