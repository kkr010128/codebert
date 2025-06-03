x,n =map(int,input().split())
if n ==0:
    print(x)
    exit()
p =list(map(int,input().split()))
l = []
for i in range(51):
    if x-i not in p and x+i not in p:
        print(min(x-i,x+i))
        exit()
    elif x-i not in p and x+i in p:
        print(x-i)
        exit()
    elif x-i in p and x+i not in p:
        print(x+i)
        exit()