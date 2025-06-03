s=input()
for _ in range(int(input())):
    a=input().split()
    i,j=map(int, a[1:3])
    if a[0] == "print":
        print(s[i:j+1])
    elif a[0] == "reverse":
        t1=s[0:i]
        t2=list(s[i:j+1])
        t2.reverse()
        t3=s[j+1:]
        s=t1+"".join(t2)+t3
    else:
        s=s[0:i]+a[3]+s[j+1:]