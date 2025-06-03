x,n=map(int,input().split())
p=set(list(map(int,input().split())))

if x not in p :
    print(x)
    exit()
i=1
while True:
    if x-i not in p:
        print(x-i)
        exit()
    if x+i not in p:
        print(x+i)
        exit()
    i+=1
