n,k=map(int, input().split())
list=list(map(int, input().split()))
count = 0
elem=0
for i in list : 
    if i >=k: 
        count +=1
    elem+=1
print(count)
