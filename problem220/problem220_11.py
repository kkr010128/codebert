lis=list(input().split())
num=list(map(int,input().split()))
num[lis.index(input())]-=1
print(str(num[0])+" "+str(num[1]))
