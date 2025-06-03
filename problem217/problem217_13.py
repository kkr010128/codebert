import sys
n=int(input())
data=list(map(int,input().split()))
for i in data:
    if i%2==1:
        continue
    if i%3!=0 and i%5!=0:
        print("DENIED")
        sys.exit()
print("APPROVED")