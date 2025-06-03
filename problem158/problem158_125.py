k=int(input())
a,b = map(int, input().split())

if a%k==0:
    print("OK")
    exit()

if a+k-a%k<=b:
    print("OK")
else:
    print("NG")
