X=int(input())
cnt=0
for i in range(1,10**7):
    cnt+=X
    if cnt%360==0:
        print(i)
        break