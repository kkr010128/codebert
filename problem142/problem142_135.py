n=list(input())
n=n[::-1]
k=int(n[0])


if k==3:
    print("bon")
elif k==2 or k==4 or k==5 or k==7 or k==9:
    print("hon")
else:
    print("pon")