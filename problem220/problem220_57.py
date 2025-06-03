l1=input().split()
l2=list(map(int,input().split()))
l2[l1.index(input())]-=1
print(" ".join(str(x) for x in l2))