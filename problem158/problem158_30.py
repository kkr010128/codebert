k = int(input())
a,b = map(int,input().split())
count = 1
flag = 0
while k * count <= b:
    if k * count >= a and k * count <= b:
        flag = 1
        count += 1
    else:
        count += 1
if flag == 1:
    print("OK")
else:
    print("NG")