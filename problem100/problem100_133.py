X=int(input())
count=8
for i in range(600,2001,200):
    if X<i:
        print(count)
        exit()
    count-=1