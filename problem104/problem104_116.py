l,r,f = map(int,input().split())
count = 0 
for i in range(l,r+1):
    if i % f == 0 :
        count = count + 1 
print(count)