k = int(input())
a, b = map(int, input().split(" "))
ngflag = True
while(a <= b):
    if a % k == 0:
        print("OK")
        ngflag = False
        break
    a += 1
if ngflag:
    print("NG")
