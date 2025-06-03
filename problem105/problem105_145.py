n=map(int,input().split())
a=list(map(int,input().split()))
 
N=0
new_a=a[::2]
 
for i in new_a:
    if i%2==0:
        N += 1
 
print(len(new_a)-N)