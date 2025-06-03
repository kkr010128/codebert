num=[]
num=list(map(int,input().split()))
for i in range(5):
    if num[i]==0:
        print(i+1)
        break
    else:
        continue
