N = int(input())
a = list(map(int,input().split()))
i=0
for x,y in enumerate (a):
    b=x+1
    if b%2!=0 and y%2!=0:
        i+=1
print(i)