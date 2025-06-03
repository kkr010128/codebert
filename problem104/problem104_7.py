li =list(map(int,input().split()))
n =li[0]
m =li[1]
k =li[2]
count =0
for i in range(n,m+1):
    if i%k ==0:
        count +=1

print(count)
