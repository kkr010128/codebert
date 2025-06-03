n=int(input())
alist=list(map(int,input().split()))

counter = 0
for i , a in enumerate(alist):
    if (i+1)%2 == 1 and a % 2 == 1:
        counter += 1

print(counter)
