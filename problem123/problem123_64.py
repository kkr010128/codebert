# n=int(input())
# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
#ls=list(map(int,input().split()))
#for i in range(m):
# for _ in range(int(input())):
#from collections import Counter
#from fractions import Fraction
n=int(input())
arr=list(map(int,input().split()))
var=arr[0]
for i in range(1,n):
    var^=arr[i]
for i in range(n):
    print(arr[i]^var,end=" ")

#ls = [list(map(int, input().split())) for i in range(n)]
#for _ in range(int(input())):
