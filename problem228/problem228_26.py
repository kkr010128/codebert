H=int(input())
if H==1:
    print(1)
else:
    i=1
    count=1
    while H//2!=1:
        i*=2
        count+=i
        H=H//2
    i*=2
    count+=i
    print(count)
