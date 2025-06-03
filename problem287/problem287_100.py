N=int(input())
count=0

for i in range(1,10):
    for j in range(1,10):
        if N/i==j:
            count+=1
        else:
            count=count

if count==0:
    print("No")
else:
    print("Yes")
