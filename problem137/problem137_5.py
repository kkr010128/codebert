N = int(input())
A_list = [0]*N
B_list = [0]*N
for i in range(N):
    A_list[i],B_list[i] = map(int,input().split())

A_list.sort()
B_list.sort()

if N%2 == 1:
    print(B_list[(N-1)//2] - A_list[(N-1)//2] + 1)
else:
    big = (B_list[N//2] + B_list[N//2-1])/2
    small = (A_list[N//2] + A_list[N//2-1])/2
    print(int((big-small)*2 + 1))