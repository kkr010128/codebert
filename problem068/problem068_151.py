str = input()
q = int(input())
for i in range(q):
    s = input().split(" ")
    cmd,a,b = s[0],int(s[1]),int(s[2])
    if(cmd=="print"):
        print(str[a:b+1])
    elif(cmd=="reverse"):
        str = str[:a]+str[a:b+1][::-1]+str[b+1:]
    else:
        str = str[:a]+s[3]+str[b+1:]