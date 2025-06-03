n1=int(input())
l1=list(input().split())

n2=int(input())
l2=list(input().split())


cnt=0
for x in l2:
    if x in l1:
        cnt=cnt+1


print(cnt)

