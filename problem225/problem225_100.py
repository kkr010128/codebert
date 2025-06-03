H,A=map(int,input().split())
if 1<=H<=10000 and 1<=A<=10000:
    print(H//A+1 if H%A!=0 else int(H/A))