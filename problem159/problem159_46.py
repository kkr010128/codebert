x=int(input())

c=100
i=0
while True:
    i+=1
    c=c+c//100
    if x<=c:
        print(i)
        exit()
