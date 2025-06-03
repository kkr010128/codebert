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

a=""

l=[]
while n>0:
    n-=1
    mod=n%26
    n//=26
    l.append(mod)
#print(l)
for i in range(len(l))[::-1]:
    a+=chr(97+l[i])
print(a)