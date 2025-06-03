N=int(input())

A=list(map(int,input().split()))

flg=True
for i in A:
    if i%2==0:
        if i%3==0 or i%5==0:
            pass
        else:
            flg=False
            break
    else:
        pass

if flg:
    print("APPROVED")
else:
    print("DENIED")    