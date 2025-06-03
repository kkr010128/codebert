s=input()
times=int(input())
for _ in range(times):
    order=input().split()
    a=int(order[1])
    b=int(order[2])
    if order[0]=="print":
        print(s[a:b+1])
    elif order[0]=="reverse":
        s=s[:a]+s[a:b+1][::-1]+s[b+1:]
    else :
        s=s[:a]+order[3]+s[b+1:]
    
