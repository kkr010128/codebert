h = int(input())

cnt = 0
num = 1
while h!=1:
    cnt += num
    num *= 2
    h = h//2
else:
    cnt += num
print(cnt)
