import sys
#a,b=map(int,input().split())
a,b,c=map(int,input().split())
if a<b:
    if b<c:
        print("Yes")
        sys.exit()
print("No")