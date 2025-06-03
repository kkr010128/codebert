import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''


n=int(input())
a=list(map(int,input().split()))
s=1000
for i in range(n-1):
    if a[i]<a[i+1]:
        s+=(a[i+1]-a[i])*(s//a[i])
    
print(s)