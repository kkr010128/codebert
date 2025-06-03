n=list(map(int,input().strip().split()))
m=list(map(int,input().strip().split()))
for i in range(n[0]-n[1]):
    if(m[i+n[1]]>m[i]):
        print("Yes")
    else:
        print("No")