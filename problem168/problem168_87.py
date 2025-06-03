N,M=map(int,input().split())
A=input()
List_A=A.split()
day=0
for i in range(0,M):
    day=day+int(List_A[i])

if N>=day:
    print(N-day)
else:
    print(-1)