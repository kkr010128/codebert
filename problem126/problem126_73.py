x=list(map(int,input().split()))
for i in range(len(x)):
    if x[i]==0:
        su=i+1
print(su)