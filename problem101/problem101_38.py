A,B,C=map(int,input().split())
K = int(input())

flag = False
cnt = 0

while(A>=B):
    if cnt > K :
        break
    B = 2*B
    cnt += 1

while(B>=C):
    if cnt >= K:
        break
    C = 2*C
    cnt += 1

#print(A,B,C)
if A < B and B < C:
    flag = True

if flag:
    print("Yes")
else:
    print("No")