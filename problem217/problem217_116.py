n=int(input())
l=list(map(int,input().split()))
f=0
for i in l:
    if(i%2==0):
        if(i%3!=0 and i%5!=0):
            f=1
            break
if(f==1):
    print("DENIED")
else:
    print("APPROVED")
