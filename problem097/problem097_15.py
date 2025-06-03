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

k=int(input())
if k%2==0:
    print("-1")
    sys.exit()

flg=False
cnt=0
a=7
for i in range(k):
    cnt+=1
    a%=k
    if a%k==0:
        print(cnt)
        sys.exit()
    a*=10
    a+=7

if not flg:
    print(-1)