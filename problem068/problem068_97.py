s=input()
n=int(input())
for _ in range(n):
    tmp=list(map(str,input().split()))
    a,b=int(tmp[1]),int(tmp[2])+1
    if tmp[0]=="print":
        print(s[a:b])
    elif tmp[0]=="reverse":
        stmp=s[a:b]
        s=s[:a]+stmp[::-1]+s[b:]
    else:
        p=tmp[3]
        s=s[:a]+p+s[b:]
