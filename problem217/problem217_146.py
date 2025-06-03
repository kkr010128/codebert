N = int(input())
A = map(int,input().split())

flag = True
for a in A:
    if a%2==0:
        if(a%3 == 0 or a%5 == 0):
            pass
        else:
            flag = False
if(flag):
    print("APPROVED")
else:
    print("DENIED")